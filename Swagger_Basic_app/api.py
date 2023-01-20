from flask import Flask,request,jsonify,Blueprint
import json
from flask_restplus import Api,fields,reqparse,Resource,Namespace

app =  Flask(__name__)


api = Api(app,version='1.0',title='Api Trail',description='Api Free Version or practice')

upload_parser = api.parser()
upload_parser.add_argument("a",type=int,help='a varible is a type of int',required=True)
upload_parser.add_argument("b",type=int,help='b varible is a type of int',required=False)



@api.route('/app/')
@api.doc(responses={ 200: 'OK', 404: 'Not able to post',502:"Server error"})
@api.expect(upload_parser)
class Asset(Resource):
    def post(self):
        obj  = upload_parser.parse_args()
        a = int(obj.get('a'))
        return {"result":a**2,"method":"POST"}
    
    def get(self):
        obj  = upload_parser.parse_args()
        a = int(obj.get('a'))
        return {"result":a**2,"method":"GET"}

    def delete(self):
        obj  = upload_parser.parse_args()
        a = int(obj.get('a'))
        return {"result":a**5,"method":"DELETE"}
if __name__=="__main__":
    app.run(debug=True,port=5000)