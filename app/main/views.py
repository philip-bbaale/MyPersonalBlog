from flask import render_template, url_for, flash, redirect, request, abort
from . import main
import requests


@main.route("/")
@main.route("/home")
def home():
    random_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    quote_response = requests.get(random_quote_url) 
    quote_data = quote_response.json()
    return render_template('home.html', title='Home', quote_data = quote_data)
    <--->

@main.route("/about")
def about():
    return render_template('about.html', title='About')
