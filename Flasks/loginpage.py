#creating flask application
from flask import Flask
app= Flask(__name__) #creating flask application
@app.route('/') #/ means homepage
def home():
    return 'Welcome to the home page'

#@app.route('/second')#another page, Get method
@app.route('/second/<name>') #another page but /second wont work unless we provide /second/somename, that is post method
#def second(name):
#    print(name)
#    return 'Welcome to the second page'

def second(name):
    length=len(name)
    if length>5:
        return 'you have good name'
    else:
        return 'its a bad name!'
#calling App
if __name__ == '__main__':
    app.run(debug=True) #debug continuosly checks for updates to code and gives output accordingly
