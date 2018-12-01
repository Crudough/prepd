from flask import Flask, render_template, url_for
import prepd_tools
import json 

app = Flask(__name__)

@app.route('/')
def prepd():
	return render_template('home.html')

@app.route('/the-pass')
def thePass():
	return render_template('pass.html')

@app.route('/metro-flyer')
def metro():
	store = 'Metro'
	j = prepd_tools.get_JSON('english', 'metro', 'K7L4A5')
	#images = prepd_tools.get_img(json)
	names, imgs = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, names=names)

@app.route('/superstore-flyer')
def superstore():
	store = 'Great Canadian Superstore'
	return render_template('flyer.html', store=store, images=images)

@app.route('/no-frills-flyer')
def no_frills():
	store = 'No Frills'
	return render_template('flyer.html', store=store, images=images)

@app.route('/sobeys-flyer')
def sobeys():
	store = 'Sobeys'
	return render_template('flyer.html', store=store, images=images)