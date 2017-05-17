from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'all_friends')

@app.route('/')
def index():
    friends = mysql.query_db("select id, name, age, friend_since from friends")


    return render_template('index.html', friends=friends)

@app.route('/create', methods=["POST"])
def create():
    query = "insert into friends (name, age, friend_since) values (:name, :age, :friend_since)"

    data = {
        'name': request.form["name"],
        'age': request.form["age"],
        'friend_since': request.form["friend_since"]
    }

    result = mysql.query_db(query, data)

    print result

    return redirect('/')

app.run(debug=True)
