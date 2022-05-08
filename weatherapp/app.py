import json
from flask import Flask, render_template, request, url_for, send_file, Response
from werkzeug.utils import redirect
import boto3
import json
from temperature import get_dict_7_days
from downlaod_cv import download_cv

app = Flask(__name__)

path = 'D:/Desktop/'

dict_ = {}
keep_location = ""


@app.route('/', methods=["GET", "POST"])
def index():
    global keep_location
    global dict_
    if request.method == "POST":
        location_ = request.form.get("location")
        if location_ == "":
            return redirect(url_for("error", location=location_))
        dict_ = get_dict_7_days(location_)
        keep_location = location_
        if dict_ is None:
            return redirect(url_for("error", location=location_))
        print(dict_)
        return render_template("index.html", dict_=dict_, location=location_)
    else:
        return render_template("home.html")


@app.route('/keep_weather')
def keep_weather():
    update_dynamodb()
    return render_template("home.html")


@app.route('/error')
def error():
    location = request.args['location']
    return render_template("error.html", location=location)


@app.route('/about-project')
def about():
    return render_template("about-project.html")


# @app.route('/download')
# def download():
#     download_cv()
#     return render_template("about-project.html")


@app.route('/download')
def downloadFile():
    file = download_cv()
    return Response(file['Body'].read(), mimetype='application/pdf',
                    headers={"Content-Disposition": "attachment;filename" "=CV-Elyasaf-Lehrer.pdf"})
