from numpy import require
import pandas as pd
from flask import Flask,request,jsonify,Blueprint
from flask_restplus import Api,fields,reqparse,Resource
import logging

import Pic_Suggestion.suggestion  as pic

document = Blueprint('api', __name__,url_prefix='/api')

"""
logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
file_handler = logging.FileHandler("log/api.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)"""
log = logging.getLogger('app')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
file_handler = logging.FileHandler("log/app.log")
file_handler.setFormatter(formatter)
log.addHandler(file_handler)

api = Api(document,version='1.0',title="Api for Pic Suggestion",description="Team Alone ")


image_data = api.namespace('image')


image_parser = api.parser()
image_parser.add_argument('emotion',required=False,type=str,help='Suggest image by emotion (default - None|Neutral)')

@image_data.route("/")
@image_data.doc(responses={ 200: 'OK', 404: 'Not able to post'})
@image_data.expect(image_parser)
class ImageData(Resource):
    def post(self):
        try: 
            args = image_parser.parse_args()
            emo = args.get('emotion','neutral')
            return {"emotion" :emo, "images":pic.get_images(emo)}

        except Exception as e:
            log.error(e.__doc__)
            pass