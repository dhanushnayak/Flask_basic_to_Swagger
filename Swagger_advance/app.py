from flask import Flask
from apis import documents

app = Flask(__name__)
app.register_blueprint(documents)

@app.route("/",methods=['GET'])
def index():
    return "Api 1.0 loading..."
    
if __name__ == '__main__':
    app.run(debug=True)