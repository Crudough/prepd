from flask import Flask, render_template, url_for, request
import prepd_tools
import json 
evan = "V9L6A8"
app = Flask(__name__)

@app.route('/')
def prepd():
	return render_template('home.html')

@app.route('/the-pass')
def thePass():
	return render_template('pass.html')

@app.route('/find-ingredients', methods=['GET', 'POST'])
def findingredients():
	if request.method == 'POST':
		j = prepd_tools.get_JSON('english', '*', 'M9B4J6')
		result = request.form['ingredients']
		result = "".join(result.split())
		result = result.split(',')
		find = prepd_tools.find(result, j)
		imgs = prepd_tools.get_img(find)
		names = prepd_tools.get_name(find)
		length = len(imgs)
		print(names)
		return render_template('find_ingredients.html', searched=True, images=imgs,
								names=names, length=length)

	return render_template('find_ingredients.html', searched=False, results=None)

@app.route('/metro-flyer')
def metro():
	store = 'Metro'
	j = prepd_tools.get_JSON('english', 'metro', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/superstore-flyer')
def superstore():
	store = 'Great Canadian Superstore'
	j = prepd_tools.get_JSON('english', 'superstore', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/no-frills-flyer')
def no_frills():
	store = 'No Frills'
	j = prepd_tools.get_JSON('english', 'nofills', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/sobeys-flyer')
def sobeys():
	store = 'Sobeys'
	j = prepd_tools.get_JSON('english', 'sobeys', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/dell-flyer')
def dell():
	store = 'Dell Canada'
	j = prepd_tools.get_JSON('english', 'dell', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/newegg-flyer')
def newegg():
	store = 'Newegg Canada'
	j = prepd_tools.get_JSON('english', 'staples', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/best-buy-flyer')
def bestbuy():
	store = 'Best Buy Canada'
	j = prepd_tools.get_JSON('english', 'bestbuy', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/ikea-flyer')
def ikea():
	store = 'IKEA'
	j = prepd_tools.get_JSON('english', 'ikea', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))

@app.route('/home-hardware-flyer')
def homehardware():
	store = 'Home Hardware'
	j = prepd_tools.get_JSON('english', 'homehardware', 'M9B4J6')
	images = prepd_tools.get_img(j)
	names = prepd_tools.get_name(j)
	return render_template('flyer.html', store=store, images=images, 
							names=names, length=len(images))
