# -*- coding=utf-8 -*-
"""
flask学习
"""
from flask import Flask
from flask import request
from flask import make_response
from flask.ext.script import Manager
from flask import render_template
from flask import redirect
from flask import abort


app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    resp = make_response("<h1>Hello World!</h1>")
    resp.set_cookie("answer", "23")
    return resp


@app.route("/user")
def user():
    # return redirect("https://www.baidu.com")
    # return "<h1> Hello ,%s!</h1>"% request.headers.get("User-Agent")
    return render_template("user.html", name="hahah")


@app.route("/user/<id>")
def get_user(id):
    # abort(404)
    return "<h1> Hello ,%s!</h1>"% request.headers.get("User-Agent")


if __name__ == "__main__":
    manager.run()
