from flask import Flask, render_template, request
from flask_mail import Mail, Message

from send_mail.sendmail import send_the_mail
app = Flask(__name__)

mail = Mail(app)


data = {"Maths": 100, "Data structure": 100, "CO": 100, "Python": 100}
@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/")
def home():
    return render_template("index.html", data=data)

@app.route("/update", methods=["POST"])
def update_maths():
    global data
    
    if request.form.get("absent"):
        data["Maths"] -= 10
    a_percent = data["Maths"]/100*100
    if(a_percent<75):
        send_the_mail(a_percent,f"Your attendance percentage in Maths is {a_percent}%. You will not be allowed to write internals if you dont attend the classes!")
    elif(a_percent<85):
        send_the_mail(a_percent,f"Your attendance percentage in Maths is {a_percent}%. Your attendence is less maintain it!")
    
    return render_template("index.html", data=data)

@app.route("/update2", methods=["POST"])
def update_data_structure():
    global data
    if request.form.get("absent2"):
        data["Data structure"] -= 10
    a_percent = data["Data structure"]/100*100
    if(a_percent<75):
        send_the_mail(a_percent,f"Your attendance percentage in Data Structure is {a_percent}%. You will not be allowed to write internals if you dont attend the classes!")
    elif(a_percent<85):
        send_the_mail(a_percent,f"Your attendance percentage in Data Structure is {a_percent}%. Your attendence is less maintain it!")
    return render_template("index.html", data=data)

@app.route("/update3", methods=["POST"])
def update_co():
    global data
    if request.form.get("absent3"):
        data["CO"] -= 10
    a_percent = data["CO"]/100*100
    if(a_percent<75):
        send_the_mail(a_percent,f"Your attendance percentage in CO is {a_percent}%. You will not be allowed to write internals if you dont attend the classes!")
    elif(a_percent<85):
        send_the_mail(a_percent,f"Your attendance percentage in CO is {a_percent}%. Your attendence is less maintain it!")
    return render_template("index.html", data=data)

@app.route("/update4", methods=["POST"])
def update_python():
    global data
    
    if request.form.get("absent4"):
        data["Python"] -= 10
    a_percent = data["Python"]/100*100
    if(a_percent<75):
        send_the_mail(a_percent,f"Your attendance percentage in Python is {a_percent}%. You will not be allowed to write internals if you dont attend the classes!")
    elif(a_percent<85):
        send_the_mail(a_percent,f"Your attendance percentage in Python is {a_percent}%. Your attendence is less maintain it!")
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(port=5001,debug=True)