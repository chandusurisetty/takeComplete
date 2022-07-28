

from numpy import take
import pandas as ps
import json
from flask import Flask, redirect, render_template, request, url_for
import json
import os
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key = "i am chandu"
Bootstrap(app)

nameLIst = []
dir_path = "challenges/"
res = os.listdir(dir_path)
for eachfile in res:

    nameLIst.append(eachfile.split(".")[0])


def jsondata(task):
    with open(f'challenges/{task}.json') as files:

        return json.load(files)


@app.route("/")
def home():

    return render_template("home.html", nameLIst=nameLIst)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        cname = request.form['challengeName']
        days = request.form['days']

        with open(f'challenges/{cname}.json', mode='w')as files:
            files.write('{"days":'+days+',"works":{}}')
            nameLIst.append(cname)
        return redirect(url_for('home'))

    return render_template('create.html')


@ app.route("/challenge/<task>", methods=["GET", "POST"])
def challenge(task):

    if request.method == "POST":

        json_bar = json.dumps(request.form, indent=4)
        data = jsondata(task)
        with open(f"challenges/{task}.json", mode="w", encoding="utf-8")as files:

            files.write(
                '{"days":'+str(data["days"])+',"works":'+json_bar+'}')

        return redirect(url_for('home'))
    data = jsondata(task)

    return render_template("workout.html", task=task, data=data)


if __name__ == "__main__":
    app.run(debug=True)
