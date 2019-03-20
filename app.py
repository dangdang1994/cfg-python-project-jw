#from flask import Flask, render_template
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")
 
@app.route("/<name>")
def say_name(name):
  # return "hello {}".format(name)
  #return f"hello {name}"
  return render_template("index.html", user=name)
  
#@app.route("/JKF")
#def say_hello1():
 # return render_template("index1.html")

#@app.route("/JKF/AAA")
#def say_hello2():
 # return render_template("index.html")
@app.route("/feedback", methods=["POST"])#若不加post所输入的内容将显示在IP地址中
def get_feedback():
 
  data = request.values

  return render_template("feedback.html", form_data=data)
  
app.run(debug=True)

