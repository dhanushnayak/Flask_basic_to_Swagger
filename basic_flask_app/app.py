from flask import Flask,request,jsonify,Blueprint
import json
from flask_restplus import Api,fields,reqparse,Resource

app =  Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "Hello World!"

@app.route("/name/<name>",methods=["GET"])
def get_name(name):
    return f"Hello {name}"


@app.route("/name/",methods=["GET"])
def get_name1():
    a = request.args.get("fname",'Fname not there')
    b = request.args.get("lname","Lname is not there")
    d = {"fname":a,"lname":b}
    return jsonify(d)

def add(a,b):
    return a+b

@app.route("/cal",methods=['POST'])
def cal():
    obj = request.get_data()
    obj = json.loads(obj)
    a = int(obj.get('a',0))
    b = int(obj.get('b',0))
    method = obj.get('method','add')
    if method=='add': c= add(a,b)
    if method=='sub': c=  a-b
    output = {"method":method,'a':a,'b':b,'result':c}
    return output

if __name__=="__main__":
    app.run(debug=True,port=5001)