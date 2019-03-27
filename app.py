from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_name(name):
  # return "hello {}".format(name)
  return f"hello {name}"

  
@app.route("/JKF")
def say_hello1():
  return render_template("index1.html")

@app.route("/JKF/AAA")
def say_hello2():
  return render_template("index.html")

#app.run(debug=True)

if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)