import os
import smtplib
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # environment variables to set up or replaced via hardcoded text
    server.login(os.getenv("MY_EMAIL"), os.getenv("MY_PASSWORD"))

    # sender and receiver's emails and message to be replaced
    server.sendmail(sender, receiver, message)
    return render_template("success.html")
