"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request, url_for
from flask_restplus import Api
import os

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest

from werkzeug.utils import secure_filename

import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from flask import current_app as App
from pydub import AudioSegment


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
        f.save(filename)

        sound_plot(filename, os.path.join(App.config['STORAGE_DIR'], 'original.png'))

        audio = AudioSegment.from_wav(filename)
        duration = audio.duration_seconds

        return {'success': True, 'duration': duration}, 201


@api_rest.route('/resources/waveform')
class SoundWaveImage(BaseResource):

    def get(self):
        audio = AudioSegment.from_wav(os.path.join(App.config['UPLOAD_DIR'], "audio.wav"))
        returnModifiedFile = False

        if 'slicing' in request.args:
            returnModifiedFile = True
            slicing = request.args.get('slicing') * 1000
            audio = audio[:slicing]

        if 'repeat' in request.args:
            returnModifiedFile = True
            repeat = request.args.get('repeat')
            audio = audio * repeat

        if 'loudness' in request.args:
            returnModifiedFile = True
            loudness = request.args.get('loudness')
            audio = audio + loudness

        if 'fade' in request.args:
            returnModifiedFile = True
            fade = request.args.get('fade')
            audio = audio.fade_in(fade)

        if 'crossfading' in request.args:
            returnModifiedFile = True
            crossfading = request.args.get('crossfading')
            duration = audio.duration_seconds
            beginning = audio[:duration // 2]
            end = audio[duration // 2:]
            audio = beginning.append(end, crossfade=crossfading)

        if 'invert' in request.args:
            returnModifiedFile = True
            invert = request.args.get('invert')
            if invert == 'true':
                audio = audio.reverse()
                
        if returnModifiedFile:
            modified_filepath = os.path.join(App.config['STORAGE_DIR'], 'modified.wav')
            audio.export(modified_filepath)
            sound_plot(modified_filepath, os.path.join(App.config['STORAGE_DIR'], 'modified.png'))

        image_url = url_for('static', filename='modified.png') if returnModifiedFile else url_for('static',
                                                                                                  filename='original.png')

        return {'link': image_url, 'modified': returnModifiedFile}
