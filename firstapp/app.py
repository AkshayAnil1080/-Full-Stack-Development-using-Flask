from flask import Flask, render_template  # import Flask class from module:flask
import os
import subprocess

#creating a new object and this object is my site.
app = Flask("techy exploring flask")

#makng  fucntions to perform the diff functionalities.


def myhello(): 
 print("flask")

@app.route("/search")  # this comes from flask
def mysearch(): 
 data = os.system("date /t")  
 print(" u are on search route ")   # print in CLI
 return("""<marquee>search...</marquee>

""" )  # print in Web GUI.


@app.route("/date")
def currdate():
 data1 = subprocess.getoutput("date /t")
 return(data1)


# @ comes from pyhton known as decorator -> helps in calling the function
@app.route("/email")  # this comes from flask known as Route , 
def myemail(): 
 print("  u are on mail route ")
 return render_template("s.html")