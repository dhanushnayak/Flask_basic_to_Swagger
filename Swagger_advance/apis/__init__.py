from flask_restplus import Api
from flask import Blueprint
from .Cars import car
from .Person import person

documents = Blueprint("Api",__name__,url_prefix='/docs')

api = Api(
    documents,
    title='MY Advance Api',
    version='1.0',
    description='A description of car and person details',
)

api.add_namespace(car)
api.add_namespace(person)