"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request, url_for
from flask_restplus import Api
import os
import random

import matplotlib
from . import layer_viz

matplotlib.use('Agg')

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest
import logging

from werkzeug.utils import secure_filename

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from flask import current_app as App
from pydub import AudioSegment
import shutil

logger = logging.getLogger('SoundViz-resources.py')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)


def sound_plot(wav_file, img_file):
    samplerate, data = wavfile.read(wav_file)
    times = np.arange(len(data)) / float(samplerate)

    data = [row[0] for row in data]
    # plot making starts
    plt.figure(figsize=(30, 4))

    with open('out', 'w') as f:
        f.write(str(list(data)))

    plt.fill_between(times, data, color='m')
    plt.xlim(times[0], times[-1])
    plt.xlabel('time(s)')
    plt.ylabel('amplitude')
    plt.savefig(img_file, dpi=100)
    return


@api_rest.route('/resources/audio')
class Audio(BaseResource):
    """ Sample Resource Class """

    def post(self):
        # global file_name
        import json
        logger.debug(request.data)
        vals = json.loads(request.data) if request.data != b'' else {}

        _hash = str(random.getrandbits(64))
       
        if 'fname' in vals:
            old_hash = vals['hash']
            filename = vals['fname']
            filename_abs = os.path.join(App.config['STORAGE_DIR'], f"{old_hash}{filename}.wav")
            new_fname = os.path.join(App.config['STORAGE_DIR'], f"{_hash}original.wav")
            shutil.copy(filename_abs, new_fname)
            print(new_fname)
            filename = new_fname

        else:
            logger.debug("loading files")
            f = request.files['file']

            filename = os.path.join(App.config['STORAGE_DIR'], f"{_hash}original.wav")
            print(filename)
            logger.debug(filename)
            f.save(filename)
        
        logger.info("predicting")
        response = layer_viz.digit_predict(filename, _hash)
        logger.debug(response)

        sound_plot(filename, os.path.join(App.config['STORAGE_DIR'], _hash + 'original.png'))

        audio = AudioSegment.from_wav(filename)
        duration = audio.duration_seconds

        return {'success': True, 'duration': duration, 'link_template': url_for('static', filename='dummy'),
                'data': response['data'], 'hash': _hash}, 201


def transform(type, value, audio):
    if not value:
        return audio

    if type == 'slicing':
        logger.debug("slicing: {}".format(value))
        audio = audio[:value]

    elif type == 'crossfading':
        logger.debug("crossfading {}".format(value))
        duration = len(audio)
        beginning = audio[:duration // 2]
        end = audio[duration // 2:]
        audio = beginning.append(end, crossfade=value)

    elif type == 'repeat':
        logger.debug("repeat {}".format(value))
        audio = audio * value

    elif type == 'loudness':
        logger.debug("loudness {}".format(value))
        audio = audio + value

    elif type == 'fade':
        logger.debug("fade {}".format(value))
        audio = audio.fade_in(value)

    elif type == 'invert':
        logger.debug("invert {}".format(value))
        audio = audio.reverse()

    return audio


@api_rest.route('/resources/waveform')
class SoundWaveImage(BaseResource):
    transform_types = 'slicing crossfading repeat loudness fade invert'

    @staticmethod
    def slice(audio, sliceStart, sliceEnd):
        duration = len(audio)
        start = int((sliceStart / 100) * duration)
        end = min(int((sliceEnd / 100) * duration), duration)
        logger.debug("slicing: {}, {}".format(start, end))
        return audio[start: end]

    @staticmethod
    def crossfade(audio, crossfadeStart, crossfadeEnd):
        duration = len(audio)
        start = int((crossfadeStart / 100) * duration)
        end = min(int((crossfadeEnd / 100) * duration), duration)

        return audio[: start].append(audio[end:], crossfade=max(0, end - start))

    @staticmethod
    def fade(audio, fade):
        logger.debug("fade {}".format(fade))
        return audio.fade_in(fade)

    @staticmethod
    def loud(audio, loud):
        logger.debug("loud {}".format(loud))
        return audio + loud

    @staticmethod
    def repeat(audio, repeat):
        logger.debug("repeat {}".format(repeat))
        return audio * (repeat + 1)

    def get(self):
        logger.info("started get")
        params = request.args
        _hash = str(params.get('hash'))
        fname = params.get('filename')
        audio = AudioSegment.from_wav(os.path.join(App.config['STORAGE_DIR'], f'{_hash}{fname}.wav'))
        modified = False

        if 'sliceStart' in params:
            audio = self.slice(audio, params.get('sliceStart', type=int), params.get('sliceEnd', type=int))
            modified = True
        elif 'crossfadingStart' in params:
            audio = self.crossfade(audio, params.get('crossfadingStart', type=int), params.get('crossfadingEnd', type=int))
            modified = True
        elif 'fade' in params:
            audio = self.fade(audio, params.get('fade', type=int))
            modified = True
        elif 'repeat' in params:
            audio = self.repeat(audio, params.get('repeat', type=int))
            modified = True
        elif 'loud' in params:
            audio = self.loud(audio, params.get('loud', type=int))
            modified = True

        filename = ""

        if modified:
            filename = 'modified{}'.format(random.randrange(500, 2000))
            modified_filepath = os.path.join(App.config['STORAGE_DIR'], _hash + filename + ".wav")
            audio.export(modified_filepath, format='wav')
            print(len(audio))
            sound_plot(modified_filepath, os.path.join(App.config['STORAGE_DIR'],_hash+ filename + ".png"))

        image_url = url_for('static', filename=filename + ".png") if modified else url_for('static',
                                                                                           filename='original.png')

        return {'filename': filename, 'modified': modified, 'duration': audio.duration_seconds}
