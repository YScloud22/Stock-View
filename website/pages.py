from flask import Blueprint, render_template, request, flash 
import sys
import praw
import re
# import stocks.py


pages = Blueprint('pages', __name__)

@pages.route('/loading', methods = ['GET','POST'])
def loadingPage():
    return render_template("loading_page.html")

@pages.route('/data', methods = ['GET','POST'])
def data():
    return render_template("data.html", 
    stock_ticker = request.form.get("stock_ticker").lower(), 
    company = request.form.get("stock_name").lower(),
    )

@pages.route('/', methods=['GET','POST'])
def home():
    stock_ticker = 'xxxx'
    company = 'xxxx'
    if request.method == 'POST':
        stock_ticker = request.form.get("stock_ticker")
        company = request.form.get("stock_name")
        if len(stock_ticker) == 0: 
            return render_template("base.html")
        if len(company) == 0: 
            return render_template("base.html")
        else: return data()
    return render_template("base.html")

@pages.route('/graph', methods = ['GET', 'POST'])
def graph(): 
    data = [("day",10), ("week",20), ("month",15)] #change numbers to actual mentions later
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("graph.html", labels=labels, values=values)