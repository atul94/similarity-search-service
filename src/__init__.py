import os
from flask import Flask
import logging

APP_NAME = "similarity-search-service-app"
SSS_APP = Flask(APP_NAME)


def config_log():
    open('/app/log/server.log', 'w+')
    log_format = '%(asctime)-15s %(levelname)s: %(message)s'
    logging.basicConfig(filename='/app/log/server.log', level=logging.INFO, format=log_format)
    SSS_APP.logger.info("### Similarity Search Service Started ###")


ROOT_MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    config_log()
except BaseException:
    SSS_APP.logger.error("Unable to initialize logging!")

try:
    CURR_ENV = os.environ['CURR_ENVIRONMENT']
except BaseException:
    SSS_APP.logger.error(
        "Current env variable not available, Falling back to PROD")
    CURR_ENV = "prod"

SSS_APP.logger.info("current env= {}".format(str(CURR_ENV)))


