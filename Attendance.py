from flask import Flask, redirect, url_for, render_template, request
import datetime
import pyrebase


config = {
    "apiKey": "AIzaSyDLCUA6er37SBBrIz-b5uGT5PTiSlyYhJE",
    "authDomain": "attendance-app-ec584.firebaseapp.com",
    "databaseURL": "https://attendance-app-ec584.firebaseio.com",
    "projectId": "attendance-app-ec584",
    "storageBucket": "attendance-app-ec584.appspot.com",
    "messagingSenderId": "636055601010",
    "appId": "1:636055601010:web:c19974b4efe84e98ef67eb",
    "measurementId": "G-PHXF9419JX"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if  request.method == "POST": 
        user = request.form["name"]
        email = request.form["email"]
        id1 = request.form["id1"]
        x = datetime.datetime.now()
        payload = {'time': str(x), 'name': user, 'email': email, 'id': id1}
        db.child('attendance-app').push(payload)
        # payload = {'time': x, 'name': user, 'email': email, 'id': id1}

        return redirect(url_for("hello_user", username=user))
        
        
    else:
        return render_template("login.html")
    

@app.route("/<username>")
def hello_user(username):
    return "Hi %s your attendance is submitted succefully" %username


if __name__ == "__main__" :
    app.run()
