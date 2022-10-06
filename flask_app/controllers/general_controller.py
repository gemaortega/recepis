from flask import render_template, session, redirect

from flask_app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')