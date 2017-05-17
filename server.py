from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    emails = mysql.query_db("select id, email, date from emails")


    return render_template('index.html', emails=emails)

@app.route('/create', methods=["POST"])
def create():
    query = "insert into emails (email, date) values (:email, now())"

    data = {
        'email': request.form["email"],
    }

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        result = mysql.query_db(query, data)
    return redirect('/')




    print result


app.run(debug=True)
