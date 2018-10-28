# d-DeVIS: A Gray Box Interpretable Visual Debugging Approach for Deep Sequence Learning Model
demo video- https://www.youtube.com/watch?v=v8lgR-ses_Y

## Installation

##### Before you start

* Make sure node + npm are installed (tested with npm v5.6)
* Python 3 is installed (tested with 3.6)

##### Template and Dependencies

* Clone this repository:

	```
	$ git clone https://github.com/anon-conf/d-DeVIS.git
	```

* Create a [virtual enviroment](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) (highly recommended)

* Install Python dependencies using pip or pipenv from the project directory:

	`$ pipenv install` or `pip install -r requirements.txt`

* Install npm dependencies

	```
	$ cd app/client/vue_app
	$ npm install
	```


## Development Server

While it's possible to use Flask to serve the vue app and the rest api, it is less than ideal as each change in client code would required a full rebuild and reload. Instead, we will use flask the serve the api endpoints, but we will serve the client app using the vue-cli dev server.
This combination allows you have both your backend python files and the Vue appplication files auto-reload on save.

This template also includes a few functions to help us manage the 2 servers.

This enables us to take advantage of Hot Module Replacement (HMR) and ESlint.
I think it is a small price to pay for the amount of time saved by HMR alone.

##### Api Server

From the root directory run:

```
$ python -m app serve_api
```

This will start the flask development server on `localhost:5000` and will respond to all requests on `/api.`.
This command is the same as running `python run.py`

##### Client Server

Start another terminal window, and from the same directory run:

```
$ python -m app serve_client
```

This will launch your browser and server the Vue application on `localhost:8080`. T
he vue app will hit `localhost:5000` to fetch resources.

This combination allows you have both your backend python files, as well as the Vue app files autoreload on each file save.


## Production Server

The production server uses Gunicorn to serve the entire application.
This template is configured to work with Heroku out of the box - just make sure you run `npm run build` before pushing it to your Heroku repository.

* Build your Vue Application:
```
$ python -m app build
```
This commands is a shorcut for cd-ing into `/app/client/vue_app` and running `$ npm run build`.

* Commit your code


## Features

#### Visualizing the Hidden Extracted Features of Convolutional neural networks: 
d-DeVIS provides visualization of the extracted features in each layer as image data and shows the various features of different filters of the deep Convolutional Neural Network. Users can also hear the audio representation of the hidden extracted features.
#### Interactive User Experience:
For a fluid user experience,we provide an interactive platform for the users so that they will be able to focus on the productivity of the system without any unnecessary hassle.
#### Visualizing the Audio Features as well as Modifying the Waveforms: 
Due to the complex structure of audio data, our system let's users modify various aspects of the sound property and visualize the updated waveform to provide a keen knowledge on audio data representation.
#### Custom Audio Input for Testing and Feature Distribution Visualization: 
User can not only upload a default audio data but also they can record custom speech to test the trained model. Proper distribution of the weights is also visualized.
#### Comparing different audio inputs and their hidden features: 
d-DeVIS also enables users to measure the differences of different audio inputs and check their extracted layer features.

## Abstract

The widespread usability of Deep Learning algorithms to solve various machine learning problems demands transparent decision making policy. Deep Learning algorithms are considered as a black box type learning model and they are too complex to understand. Moreover, the learning models, trained on sequential data, such as audio and video data, have intricate internal reasoning process due to their complex distribution of features. Thus, a visual simulator might be helpful to trace the internal decision making mechanisms in response to adversarial input data, and it would help to debug and design appropriate deep learning models. However, interpreting the internal reasoning of deep learning model is not well studied in the literature. In this work, we have developed a visual interactive web application, namely d-DeVIS, which helps to visualize the internal reasoning of the learning model which is trained on the audio data. The proposed system allows to perceive the behavior as well as to debug the model by interactively generating adversarial audio data point.
