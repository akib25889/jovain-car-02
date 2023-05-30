from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return """<b>Hello, World!</b>
  <button> akib</button>
  <style>
  button{
  width: 200px;
  }
  </style>"""


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
