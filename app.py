from flask import Flask, render_template

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

app.run(debug=True)

nav ul {
  list-style: none;
  font-family: Arial, sans-serif;
  font-size: 20px;
  text-align: center;
}

nav ul li {
  display: inline;
  margin-right: 20px;
}