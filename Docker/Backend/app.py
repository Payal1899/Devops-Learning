'''
Ares Application - Backend

created business logic in Business.py file and calling it in app.py file
names.txt file contains names that are being used in Business.py file to return data to app.py file
requirements.txt file contains the dependencies for the backend application, in this case, it is Flask.

In Frontend, 
we have an express app that serves html files and makes API calls to the backend to get data and display it on the frontend.
we have index.ejs file in views folder that contains the frontend code and app_copy.js file that contains the express app code.
In Docker, we have a .dockerignore file that ignores the node_modules and other unnecessary files for the frontend and backend applications.
package.json file and package-lock.json file was created when we ran npm init command in the frontend folder and installed express and axios dependencies for the frontend application.

for detailed understanding of the code, please refer to Building_app.txt file in Docker folder.
'''


from flask import Flask, request, jsonify
from Business import get_data
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello Payal From docker Flask app"

@app.route('/api', methods= ['GET'])
def api():
    data=get_data()
    #calling get_data function from Business.py file

    '''creating a dictionary to return data in json format to the frontend
    names={
        'Key':data
    }
    '''
    return jsonify(data)


if __name__== '__main__':
    app.run(port=6000,host='0.0.0.0', debug=True)
