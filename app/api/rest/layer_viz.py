import os
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from flask import current_app as App
from keras import backend as K
from keras.models import load_model
from scipy import signal
from scipy.io import wavfile

from .helper import *


# global graph,model
### Parameters ###
fft_size = 320  # window size for the FFT
step_size = fft_size / 6  # distance to slide along the window (in time)
spec_thresh = 4  # threshold for spectrograms (lower filters out more noise)
lowcut = 500  # Hz # Low cut for our butter bandpass filter
highcut = 8000  # Hz # High cut for our butter bandpass filter
# For mels
n_mel_freq_components = 64  # number of mel frequency channels
shorten_factor = 10  # how much should we compress the x-axis (time)
start_freq = 300  # Hz # What frequency to start sampling our melS from
end_freq = 8000  # Hz # What frequency to stop sampling our melS from


def static_filepath(filepath):
    return os.path.join(App.config['STORAGE_DIR'], filepath)

def first_layerr(test_input, hash):
    K.clear_session()
    first_layer = load_model(os.path.join(os.path.dirname(__file__), 'first_layer.hdf5'))
    out = first_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = first_layer.layers[0].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(static_filepath(hash+'first_distribution.png'))
    plt.clf()
    for i in range(0, 16):
        out1 = out[0, :, :, i]
        recovered_audio_orig = invert_pretty_spectrogram(out1, fft_size=int(fft_size),
                                                         step_size=int(step_size), log=True, n_iter=10)
        wavfile.write(static_filepath(hash+'first' + str(i+1) + '.wav'), 8000, recovered_audio_orig)
        plt.imsave(static_filepath(hash+'first' + str(i+1) + '.png'), out1)
        plt.clf()
    return


def second_layerr(test_input, hash):
    K.clear_session()
    second_layer = load_model(os.path.join(os.path.dirname(__file__), 'second_layer.hdf5'))
    out = second_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = second_layer.layers[4].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(static_filepath(hash+'second_distribution.png'))
    plt.clf()

    for i in range(0, 16):
        out1 = out[0, :, :, i]
        recovered_audio_orig = invert_pretty_spectrogram(out1, fft_size=int(fft_size / 2),
                                                         step_size=int(step_size), log=True, n_iter=10)
        wavfile.write(static_filepath(hash+'second' + str(i+1) + '.wav'), 8000, recovered_audio_orig)
        plt.imsave(static_filepath(hash+'second' + str(i+1) + '.png'), out1)
        plt.clf()
    return


def third_layerr(test_input, hash):
    K.clear_session()
    third_layer = load_model(os.path.join(os.path.dirname(__file__), 'third_layer.hdf5'))
    out = third_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = third_layer.layers[8].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(static_filepath(hash+'third_distribution.png'))
    plt.clf()

    for i in range(0, 16):
        out1 = out[0, :, :, i]
        recovered_audio_orig = invert_pretty_spectrogram(out1, fft_size=int(fft_size / 4),
                                                         step_size=int(step_size) - 15, log=True, n_iter=10)
        wavfile.write(static_filepath(hash+'third' + str(i+1) + '.wav'), 8000, recovered_audio_orig)
        plt.imsave(static_filepath(hash+'third' + str(i+1) + '.png'), out1)
    return


def digit_predict(filename):
    K.clear_session()
    # graph = tf.get_default_graph()
    sample_rate, samples = wavfile.read(filename)
    resampled = signal.resample(samples, int(8000 / sample_rate * samples.shape[0]))
    samples = pad_audio(resampled)
    specgram = pretty_spectrogram(samples.astype('float64'), fft_size=fft_size,
                                  step_size=int(step_size), log=True, thresh=spec_thresh)
    hash = str(random.getrandbits(64))
    # fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))
    # cax = ax.matshow(np.transpose(specgram), interpolation='nearest', aspect='auto', cmap=plt.cm.afmhot, origin='lower')
    # fig.colorbar(cax)
    # plt.title('Original Spectrogram')
    plt.imsave(static_filepath(hash + 'original_spectogram.png'), specgram)
    test_input = specgram.reshape(1, specgram.shape[0], specgram.shape[1], 1)
    first_layerr(test_input, hash)
    second_layerr(test_input, hash)
    third_layerr(test_input, hash)
    out = 0
    complete_layer = get_model()
    complete_layer.load_weights(os.path.join(os.path.dirname(__file__), 'model_weights.h5'))
    out = complete_layer.predict(test_input)
    out1 = out[0, :]
    val = np.argmax(out1).tolist()

    dic = {'data': val, 'hash': hash}
    return dic


# digit_predict()


def calculate():
    test_model = get_model()
    test_model.load_weights(os.path.join(os.path.dirname(__file__), 'model_weights.h5'))

    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.save('fourth_layer.hdf5')

    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.save('third_layer.hdf5')

    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.save('second_layer.hdf5')

    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.pop()
    test_model.save('first_layer.hdf5')
    print("calculation done.")
    K.clear_session()
    return

# calculate()
