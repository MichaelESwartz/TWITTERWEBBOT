from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import MySQLdb as mdb
from dblogin import logy


app = Flask(__name__)



@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():

    if logy(request.form['username'], request.form['password']):
        session['logged_in'] = True

    else:
        flash('wrong password!')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='10.0.0.239', port=5004)
