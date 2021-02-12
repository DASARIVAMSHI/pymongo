from flask import Flask
app = Flask(__name__) #creating the Flask class object

@app.rout('/') # decorator drfines the
def home():
    return "hello this is my first flask programm"

if __name__=='__main__':
    app.run(debug=true)