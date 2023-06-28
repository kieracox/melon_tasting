from flask import (Flask, render_template, request,flash,session,redirect)
from model import connect_to_db, db 
import crud
from datetime import datetime, timedelta
import math

from jinja2 import StrictUndefined

app = Flask(__name__, static_folder='static')
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route("/login")
def login():
    """Log in a user."""
    return redirect('/landing_page')

@app.route("/landing_page")
def landing_page():
    """View the landing page after login."""
    return render_template('res_search.html')

@app.route("/search")
def res_search():
    """Search for available reservation slots."""
    return render_template('search_results.html')

@app.route("/book_res")
def book_res():
    """Book a reservation."""
    return redirect('/landing_page')

@app.route("/reservations")
def user_res():
    """Show the reservations for a given user."""
    return render_template('user_info.html')






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)