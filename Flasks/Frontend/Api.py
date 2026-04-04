
from flask import Flask, render_template, request, redirect
import requests  #this is python lib to connect https requests

Backend_URL='http://0.0.0.0:8000'
app= Flask(__name__) #creating flask 
@app.route('/')
def first_fun():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def sec_fun():
    dict1=dict(request.form)
    print(dict1)
    requests.post(Backend_URL+'/submit', json=dict1) 
    if not dict1.get('name') or not dict1.get('email'):
        #return render_template('index.html', error="All fields required")
        render_template('index.html', error="All fields required")
        return redirect('/')
        
    else:
        collection.insert_one(dict1) #inserting data into our DB using collection
        return 'Data inserted successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6000, debug=True)  #running frontend and backend on different ports