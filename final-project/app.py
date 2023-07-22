import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")


@app.route("/")
def homepage():
    """Show homepage"""
    
    # Forget any user_id
    session.clear()

    return render_template("homepage.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get data from register form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure there is username
        if not username:
            return apology("must provide username", 400)

        # Ensure there is password
        if not password:
            return apology("must provide password", 400)

        # Ensure there is confirmation password
        if not confirmation:
            return apology("must provide confirmation password", 400)

        # Ensure password and confirmation password match
        if password != confirmation:
            return apology("password does not match confirmation", 400)
        
        # Generate hash
        hash = generate_password_hash(password)

        # Ensure that username does not exist
        try:
            # Insert new user to SQL table
            user = db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)", username, hash
            )
        except:
            return apology("username already in use", 400)

        # Remember which user has logged in
        session["user_id"] = user

        # Redirect user to application
        return redirect("/pomodoro")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to application
        return redirect("/pomodoro")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/pomodoro")
@login_required
def pomodoro():
    """Pomodoro timer"""

    # Get user id
    user_id = session["user_id"]

    # Select study, short, and long break from SQL table
    settings = db.execute("SELECT study, short, long FROM pomodoro WHERE user_id = ?", user_id)

    # Check if user has settings
    if not settings:

        # Insert default settings to SQL table
        db.execute("INSERT INTO pomodoro (user_id, study, short, long) VALUES(?, ?, ?, ?)", user_id, 25, 5, 10)

        # Select study, short, and long break from SQL table
        settings = db.execute("SELECT study, short, long FROM pomodoro WHERE user_id = ?", user_id)

    # Get values from list of dictionaries from SQL table
    study = settings[0]["study"]
    short = settings[0]["short"]
    long = settings[0]["long"]
    
    # Show settings and pass settings to the template
    return render_template("pomodoro.html", html_study=study, html_short=short, html_long=long)


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    """Settings"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # If the pomodoro settings were changed
        if request.form['action'] == 'pomodoro':

            # Get data from form
            study = request.form.get("study")
            short = request.form.get("shortBreak")
            long = request.form.get("longBreak")

            # Get user id
            user_id = session["user_id"]

            # Update new settings in SQL table
            db.execute("UPDATE pomodoro SET study = ?, short = ?, long = ? WHERE user_id = ?", study, short, long, user_id)

            # Give message to user
            flash("Pomodoro settings updated!")

            # Stay on settings page
            return redirect("/settings")
        
        # If the password was changed
        elif request.form['action'] == 'change':

            # Get data from form
            new_password = request.form.get("new_password")
            confirmation = request.form.get("confirmation")

            # Ensure there is password
            if not new_password:
                return apology("must provide a new password", 400)

            # Ensure there is confirmation password
            if not confirmation:
                return apology("must provide confirmation password", 400)

            # Ensure password and confirmation password match
            if new_password != confirmation:
                return apology("new password does not match confirmation", 400)

            # Get user id
            user_id = session["user_id"]

            # Generate hash
            hash = generate_password_hash(new_password)

            # Update new settings in SQL table
            db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, user_id)

            # Give message to user
            flash("Password changed!")

            # Stay on settings page
            return redirect("/settings")
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Get user id
        user_id = session["user_id"]

        # Select study, short, and long break from SQL table to display in form
        settings = db.execute("SELECT study, short, long FROM pomodoro WHERE user_id = ?", user_id)

        # Get username to display in form
        username_db = db.execute("SELECT username FROM users WHERE id = ?", user_id)

        # Get values from list of dictionaries from SQL table
        study = settings[0]["study"]
        short = settings[0]["short"]
        long = settings[0]["long"]
        username = username_db[0]["username"]

        return render_template("settings.html", html_study=study, html_short=short, html_long=long, html_username=username)
      
    
# Calendar routes
@app.route("/calendar", methods=["GET", "POST"])
@login_required
def calendar():
    """Calendar"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        return redirect("/add_event")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Get user id
        user_id = session["user_id"]

        # Get event details from SQL table
        event_info = db.execute("SELECT name, event_date, color FROM events WHERE user_id = ?", user_id)

        # Show calendar and pass event_info to the template
        return render_template("calendar.html", event_info=event_info)


@app.route("/add_event", methods=["GET", "POST"])
@login_required
def add_event():
    """Add an event to the calendar"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get data from form
        event_name = request.form.get("event")
        event_date = request.form.get("date")
        event_color = request.form.get("color")

        # Check that user typed name, date, and color
        if not event_name:
            return apology("must provide event name", 400)
        if not event_date:
            return apology("must provide event date", 400)
        if not event_color:
            return apology("must provide event color", 400)

        # Check that date is in MM/DD/YYYY format
        if not re.match(r"\d{2}/\d{2}/\d{4}", event_date):
            return apology("event date must be in MM/DD/YYYY format", 400)

        # Check that date is valid
        try:
            month, day, year = event_date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        except:
            return apology("event date must be in MM/DD/YYYY format", 400)
        
        # Check that color is in hex format
        if not re.match(r"#[0-9a-fA-F]{6}", event_color):
            return apology("event color must be in hex format", 400)
        
        # Get user id
        user_id = session["user_id"]

        # Insert new event to SQL table
        db.execute("INSERT INTO events (user_id, name, event_date, color) VALUES(?, ?, ?, ?)", user_id, event_name, event_date, event_color)
        
        # Give message to user
        flash("Event added!")

        # Redirect user to calendar
        return redirect("/calendar")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("add_event.html")
    

@app.route("/delete_event", methods=["GET", "POST"])
@login_required
def delete_event():
    """Add an event to the calendar"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get data from form
        event_delete = request.form.get("deleted_event")

        try:
            # Delete event from SQL table
            db.execute("DELETE FROM events WHERE name = ?", event_delete)
        except:
            return apology("event does not exist", 400)

        # Give message to user
        flash("Event deleted!")

        # Redirect user to calendar
        return redirect("/calendar")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Get user id
        user_id = session["user_id"]

        # Get event names from SQL table to display in dropdown menu
        event_names = db.execute("SELECT name FROM events WHERE user_id = ?", user_id)

        # Show delete event page and pass event_names to the template
        return render_template("delete_event.html", names=event_names)
    