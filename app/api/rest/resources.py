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
    # plot making starts
    plt.figure(figsize=(30, 4))
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
        f = request.files['file']
        filename = os.path.join(App.config['UPLOAD_DIR'], "audio.wav")
        print(filename)
        logger.debug(filename)
        f.save(filename)
        response = layer_viz.predict(filename)

        sound_plot(filename, os.path.join(App.config['STORAGE_DIR'], 'original.png'))

        audio = AudioSegment.from_wav(filename)
        duration = audio.duration_seconds

        return {'success': True, 'duration': duration, 'data': response['data'], 'hash': response['hash']}, 201

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

    def get(self):
        audio = AudioSegment.from_wav(os.path.join(App.config['UPLOAD_DIR'], "audio.wav"))
        params = request.args
        returnModifiedFile = 'slicing' in params




        for transformation in SoundWaveImage.transform_types.split(" "):
            audio = transform(transformation, params.get(transformation, type=int), audio)


        logger.debug("{}".format(len(audio)))

        filename = ""

        if returnModifiedFile :
            filename = 'modified{}'.format(random.randrange(5000, 50000))
            modified_filepath = os.path.join(App.config['STORAGE_DIR'], filename + ".wav")
            audio.export(modified_filepath, format='wav')
            print(len(audio))
            sound_plot(modified_filepath, os.path.join(App.config['STORAGE_DIR'], filename + ".png"))

        image_url = url_for('static', filename=filename+".png") if returnModifiedFile else url_for('static',
                                                                                                  filename='original.png')

        return {'link': image_url, 'modified': returnModifiedFile, 'duration': audio.duration_seconds}
