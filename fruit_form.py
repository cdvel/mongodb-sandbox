import bottle

@bottle.route('/')
def home():
	mythings = ['apple', 'banana', 'peach']
	return bottle.template('fruit_form', {'username': 'Larry', 'things' : mythings})


@bottle.post('/favorite_fruit')
def favorite_fruit():
	fruit = bottle.request.forms.get("fruit")
	if (fruit == None or fruit == ""):
		fruit = "No selection"
	
	bottle.response.set_cookie("fruit", fruit)
	bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
	fruit = bottle.request.get_cookie("fruit");
	return bottle.template('fruit_selection.tpl', {'fruit': fruit})



bottle.debug(True)
bottle.run(hosts='localhost', port=8080)
