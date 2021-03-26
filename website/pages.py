from flask import Blueprint, render_template, request, flash 
import sys

pages = Blueprint('pages', __name__)

@pages.route('/home', methods=['GET','POST'])
def home():
    return render_template("base.html")