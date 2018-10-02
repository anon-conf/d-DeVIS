from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
import IPython
from pydub import AudioSegment
from flask import Flask, render_template, jsonify, request
import numpy as np
import librosa
import os
from sklearn.model_selection import train_test_split
import glob
from pydub import AudioSegment
import IPython
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import tensorflow as tf

from keras.utils import to_categorical
from keras.layers import Input, Add, Dropout, Dense, GRU, Bidirectional, Masking, TimeDistributed, LSTM, Conv1D, \
    Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from keras.models import Model, load_model, Sequential
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import layer_utils, plot_model, to_categorical
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import InceptionV3
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from keras import backend as K
from keras import optimizers, losses, activations, models
from keras.initializers import glorot_uniform
from scipy.fftpack import fft
from scipy.io import wavfile
from scipy import signal
import keras
from keras import backend as k
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request
from werkzeug import secure_filename
from helper import *

global graph, model
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


def first_layerr(test_input):
    K.clear_session()
    first_layer = load_model('first_layer.hdf5')
    out = first_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = first_layer.layers[0].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig('first_distribution.png')
    plt.clf()
    for i in range(0, 16):
        out1 = out[0, :, :, i]
        plt.imsave('first' + str(i) + '.png', out1)
        plt.clf()
    return


def second_layerr(test_input):
    K.clear_session()
    second_layer = load_model('second_layer.hdf5')
    out = second_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = second_layer.layers[4].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig('second_distribution.png')
    plt.clf()

    for i in range(0, 16):
        out1 = out[0, :, :, i]
        plt.imsave('second' + str(i) + '.png', out1)
        plt.clf()
    return


def third_layerr(test_input):
    K.clear_session()
    third_layer = load_model('third_layer.hdf5')
    out = third_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = third_layer.layers[8].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig('third_distribution.png')
    plt.clf()

    for i in range(0, 16):
        out1 = out[0, :, :, i]
        plt.imsave('third' + str(i) + '.png', out1)
    return


def digit_predict():
    K.clear_session()
    graph = tf.get_default_graph()
    complete_layer = load_model('model_weights.hdf5')
    sample_rate, samples = wavfile.read('sliced.wav')
    resampled = signal.resample(samples, int(8000 / sample_rate * samples.shape[0]))
    samples = pad_audio(resampled)
    specgram = pretty_spectrogram(samples.astype('float64'), fft_size=fft_size,
                                  step_size=int(step_size), log=True, thresh=spec_thresh)
    test_input = specgram.reshape(1, specgram.shape[0], specgram.shape[1], 1)
    first_layerr(test_input)
    second_layerr(test_input)
    third_layerr(test_input)
    '''
    with graph.as_default():
        out = complete_layer.predict(test_input)
    out1 = out[0, :]
    val = np.argmax(out1).tolist()
    print(val)
    '''
    dic = {'data': 'val'}
    return jsonify(dic)


digit_predict()


def calculate():
    test_model = load_model('model_weights.hdf5')

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
