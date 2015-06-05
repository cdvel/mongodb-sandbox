import bottle

@bottle.route('/')
def home():
	mythings = ['apple', 'banana', 'peach']
	return bottle.template('hello_world', username= 'Larry', things=mythings)

bottle.debug(True)
bottle.run(hosts='localhost', port=8080)
