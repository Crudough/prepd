from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def prepd():
	return render_template('home.html')

@app.route('/the-pass')
def thePass():
	return render_template('pass.html')