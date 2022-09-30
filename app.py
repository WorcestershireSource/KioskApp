import os
import copy
import uuid

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from Squarecode import fetch_menu, check_out

from robotinstructions import make_drink

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Menu is a list of dicts built in squarecode.py. Terminal connects terminal
menu = fetch_menu()

basket = []

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html", menu=menu, basket=basket, total= "{:.2f}".format(totaliser() / 100))


@app.route("/cancel", methods=["GET"])
def cancel():
    for i in range(len(basket) - 1, -1, -1):
        basket.pop(i)

    return redirect("/")

@app.route("/addbasket", methods=["POST"])
def addbasket():
    basket_add_id = request.form.get("addbasket")

    for item in menu:
        if item["id"] == basket_add_id:
            # Creates a deepcopy of the item and adds it to the basket with a unique id for each item in basket  e.g. if multiple same item 
            tmp = copy.deepcopy(item)
            tmp["basket_id"] = len(basket)
            basket.append(tmp)
    
    return redirect("/")

@app.route("/removebasket", methods=["POST"])
def removebasket():
    remove_basket = request.form.get("basketremove")

    for i, item in enumerate(basket):
        if item["basket_id"] == int(remove_basket):
            basket.pop(i)
    
    return redirect("/")

@app.route("/checkout", methods=["GET"])
def checkout():
    idempotency_key = str(uuid.uuid4())
    check_out(basket, totaliser(), idempotency_key)
    
    return redirect("/cancel")




def totaliser():
    total = 0.00
    for item in basket:
        total += item["Price"]
    return total