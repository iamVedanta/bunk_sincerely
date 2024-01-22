
# importing libraries 
from flask import Flask 
from flask_mail import Mail, Message 
   
app = Flask(__name__) 
mail = Mail(app) # instantiate the mail class 
   
# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vvce22cseaiml0093@vvce.ac.in'
app.config['MAIL_PASSWORD'] = 'vvce@1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 
   

def send_the_mail(ap,warning_message): 
   msg = Message( 
                "Attendance alert", 
                sender ='vvce22cseaiml0093@vvce.ac.in@gmail.com', 
                recipients = ['callvedanta@gmail.com'] 
               ) 
   msg.body = warning_message
   mail.send(msg) 
   return 'Sent'
   
if __name__ == '__main__': 
   app.run(debug = True) 