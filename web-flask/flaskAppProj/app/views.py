from flask import jsonify
from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg="hello world!", a = 3)