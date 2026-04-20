from flask import Flask, request, jsonify
from Business import get_data
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello Payal From docker Flask app"

@app.route('/api', methods= ['GET'])
def api():
    data=get_data()
    dict={
        'data':data
    }
    return jsonify(dict)


if __name__== '__main__':
    app.run(port=6000, debug=True)
