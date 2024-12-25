from flask import Flask,request,flash,render_template,redirect
from flask_mail import Mail,Message
app =Flask(__name__,template_folder='template')
app.secret_key="2468"


app = Flask(__name__,template_folder='template')

  
# configuration of mail




@app.route("/",methods=["POST","GET"])
def index():
   app.config['MAIL_SERVER']='smtp.gmail.com'
   app.config['MAIL_PORT']=587
   app.config['MAIL_USERNAME']='thetvshop785@gmail.com'
   app.config['MAIL_PASSWORD']='sntuyiuubmoientd'
   app.config['MAIL_USE_TLS']=True
   app.config['MAIL_USE_SSL']=False

   
   mail = Mail(app)
   
   if request.method=="POST":
      if request.form.get("report")=="content":
         name=request.form.get('name')
         fmail=request.form.get('email')
         tmail = "support@thetvshop.in"
         subject = request.form.get('subject')
         message = request.form.get('message')
         message2=("Mail Sent. Thank you " ,name)
         msg=Message(subject+" from: "+fmail,body=message,sender=fmail,recipients=[tmail])
         sendmsg=Message(message2,body=" we will contact you shortly.",sender=tmail,recipients=[fmail])
         mail.send(msg)
         mail.send(sendmsg)
      elif request.form.get('for')=="Sub":
         subscribe=request.form.get('Subscribe')
         msg1=Message("Our New Subscribe",body=subscribe,sender="thetvshop785@gmail.com",recipients=["support@thetvshop.in"])
         msg2=Message("Thank You For Subscribe",body="We will update u Soon",sender="thetvshop785@gmail.com",recipients=[subscribe])
         mail.send(msg2)
         mail.send(msg1)

   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)