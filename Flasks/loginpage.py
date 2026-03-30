#creating flask application
from flask import Flask, request #request for reuest function
app= Flask(__name__) #creating flask application
@app.route('/') #/ means homepage
def home():
    return 'Welcome to the home page'

#@app.route('/second')#another page, Get method
#def Function(name):
#    print(name)
#    return 'Welcome to the second page'
'''
@app.route('/second/<name>') #another page but /second wont work unless we provide /second/somename, that is post method
def Function(name):
    length=len(name)
    if length>5:
        return 'you have good name'
    else:
        return 'its a bad name!' 
''' 
'''
@app.route('/second/<name>/<lastname>') 
def Function(name, lastname):
    result="Hello -->> "+" "+name+"  "+lastname
    return result   
'''
'''
@app.route('/second/<a>/<b>') 
def Function(a, b):
    sum=int(a)+int(b)
    result={
        'key1':sum
    }
    return result  #return cannot be int, it should be str, dict, tuple
'''
#json input
@app.route('/api') 
def Function():
    name=request.values.get('Name')
    age=request.values.get('age')
    result={
        'N':name,
        'A':age
    }
    #input for this: https://literate-telegram-97pwwrq9wv9xfxv9x-5000.app.github.dev/api?name=Payal&age=30
    return result 
#calling App
if __name__ == '__main__':
    app.run(debug=True) #debug continuosly checks for updates to code and gives output accordingly
