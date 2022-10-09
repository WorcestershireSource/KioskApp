import os
import uuid

from flask import Flask, redirect, jsonify, render_template, request
from flask_session import Session
from Squarecode import fetch_menu, check_out, cancel_checkout

from robotinstructions import make_drink

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# GLOBALS Menu is a list of dicts built in squarecode.py
menu = fetch_menu()
checkout_id = ""

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# MAIN LOGIC

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", menu=menu)

@app.route("/checkout", methods=["POST"])
def checkout():
    basket = request.get_json()
    idempotency_key = str(uuid.uuid4())

    checkout_id = check_out(basket, idempotency_key)
    return jsonify({"processed": "true"})

@app.route("/cancelchkout", methods=["GET"])
def cancelchkout():
    cancel_checkout(checkout_id)
    return redirect("/")
