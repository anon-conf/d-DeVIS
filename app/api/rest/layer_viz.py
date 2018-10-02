import os
import random

import matplotlib.pyplot as plt
import numpy as np
from flask import current_app as App
from keras import backend as K
from keras.models import load_model
from scipy import signal
from scipy.fftpack import fft
from scipy.io import wavfile


def custom_fft(y, fs):
    T = 1.0 / fs
    N = y.shape[0]
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    vals = 2.0/N * np.abs(yf[0:N//2])
    return xf, vals

def log_specgram(audio, sample_rate, window_size=20,
                 step_size=10, eps=1e-10):
    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    freqs, times, spec = signal.spectrogram(audio,
                                    fs=sample_rate,
                                    window='hann',
                                    nperseg=nperseg,
                                    noverlap=noverlap,
                                    detrend=False)
    return freqs, times, np.log(spec.T.astype(np.float32) + eps)
  
def pad_audio(samples):
    L = 16000
    if len(samples) >= L: return samples
    else: return np.pad(samples, pad_width=(L - len(samples), 0), mode='constant', constant_values=(0, 0))

def chop_audio(samples, L=16000, num=20):
    for i in range(num):
        beg = np.random.randint(0, len(samples) - L)
        yield samples[beg: beg + L]


def model_abspath(fname):
    return os.path.join(os.path.dirname(__file__),fname )


def first_layerr(test_input, hash):
    K.clear_session()
    first_layer = load_model(model_abspath('first_layer.hdf5'))
    out = first_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = first_layer.layers[0].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(os.path.join(App.config['STORAGE_DIR'], str(hash)+'first_distribution.png'))
    plt.clf()
    for i in range(0,16):
        out1 = out[0, :, :, i]
        filename = "{}first{}.png".format(hash, i)
        plt.imsave(os.path.join(App.config['STORAGE_DIR'], filename), out1)
        plt.clf()
    return


def second_layerr(test_input, hash):
    K.clear_session()
    second_layer = load_model(model_abspath('second_layer.hdf5'))
    out = second_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = second_layer.layers[4].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(os.path.join(App.config['STORAGE_DIR'], str(hash)+'second_distribution.png'))
    plt.clf()
    
    for i in range(0,32):
        out1 = out[0, :, :, i]
        filename = '{}second{}.png'.format(hash, i)
        plt.imsave(os.path.join(App.config['STORAGE_DIR'], filename), out1)
        plt.clf()
    return


def third_layerr(test_input, hash):
    K.clear_session()
    third_layer = load_model(model_abspath('third_layer.hdf5'))
    out = third_layer.predict(test_input)
    out1 = out[0, :, :, :]
    bla = third_layer.layers[8].get_weights()[0]
    plt.plot(bla.flatten())
    plt.savefig(os.path.join(App.config['STORAGE_DIR'], str(hash)+'third_distribution.png'))
    plt.clf()
   
    for i in range(0,32):
        out1 = out[0, :, :, i]
        filename = '{}third{}.png'.format(hash, i)
        plt.imsave(os.path.join(App.config['STORAGE_DIR'], filename), out1)
    return

def predict(filename):
    K.clear_session()
    print(os.path.dirname(__file__))

    complete_layer = load_model(model_abspath('cnn_final.hdf5'))
    sample_rate, samples = wavfile.read(filename)
    samples = pad_audio(samples)
    new_sample_rate = 8000
    resampled = signal.resample(samples, int(new_sample_rate / sample_rate * samples.shape[0]))
    _, _, specgram = log_specgram(resampled, sample_rate=new_sample_rate)
    test_input =  specgram.reshape(1,specgram.shape[0],specgram.shape[1],1)
    hash = random.getrandbits(64)
    first_layerr(test_input, hash)
    second_layerr(test_input, hash)
    third_layerr(test_input, hash)
    out = complete_layer.predict(test_input)
    out1 = out[0, :]
    val = np.argmax(out1).tolist()
    print(val)
    return {'data': val, hash: hash}
