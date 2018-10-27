import os
from flask import Flask
from flask_compress import Compress
import click
from flask_cors import CORS


from app.api import api_rest, api_bp
from app.client import client_bp

app = Flask(__name__, static_folder='storage')
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
CORS(app)
Compress(app)

from . import config
app.logger.info('>>> {}'.format(config.flask_config))

