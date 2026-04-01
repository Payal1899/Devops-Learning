from flask import Flask, request, render_template
from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dummy:1234@project.9kmda5y.mongodb.net/?appName=Project"
#dummy:<db_password> : provide exact pswd

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

 #request for reuest function
app= Flask(__name__) #creating flask 
@app.route('/')
def first_fun():
    return render_template('index1.html')
@app.route('/submit', methods=['POST'])
def sec_fun():
    #name=request.form.get('name')
    #email=request.form.get('email')
    #return 'Hello  '+name+'!'+'!<br> Your email is '+email

    #another way to print data on page
    #dict1=dict(request.form)
    #return dict1

if __name__ == '__main__':
    app.run(debug=True)