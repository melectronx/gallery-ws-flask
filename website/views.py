from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html", user=current_user)


@views.route('/manage/', methods=['GET', 'POST'])
def manage():

    return render_template("manage.html", user=current_user)
