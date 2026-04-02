
#create Flask api with routes to pages, use render template to goto html Form page
#create a html file with post method and HTML form with submit button, define action for submit to come to api page
#Get data from user
#create a db user in mongo db, in network access give your public ip address so that you may connect to db with this machine
#Goto cluster and click connect>connect to your application>>do basic settings and done
#you will receive URI paste it in .env(separately created file) to secure creds
#created requirements.txt for all the required import pckgs
#run command pip install -r requirements.txt to install all of them

from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv() #calling function to load uri stored in .env file
MONGO_URI = os.getenv('uri') # same variable which is passed in .env file
client = pymongo.MongoClient(MONGO_URI)#created a client by providing the URI

db = client.test#created DB named 'test' in cluster name mentioned in URI

collection = db['flask-tutorial']#created collection named 'flask-tutorial'

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


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
    #return 
    
    #inserting into DB
    dict1=dict(request.form)
    collection.insert_one(dict1) #inserting data into our DB using collection
    return 'Data inserted successfully'
if __name__ == '__main__':
    app.run(debug=True)