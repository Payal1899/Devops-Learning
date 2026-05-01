from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv() #calling function to load uri stored in .env file
MONGO_URI = os.getenv('uri') # same variable which is passed in .env file
client = pymongo.MongoClient(MONGO_URI)#created a client by providing the URI

db = client.AssignmentDocker #created DB named 'AssignmentDocker' in cluster name mentioned in URI

collection = db['AssignmentDocker']#created collection named 'AssignmentDocker'

app= Flask(__name__) #creating flask api

@app.route('/submit', methods=['POST'])
def sec_fun():
    #inserting into DB
    data = request.form.to_dict()
    collection.insert_one(data)
    return {"msg": "Data inserted successfully"}
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6001, debug=True) 