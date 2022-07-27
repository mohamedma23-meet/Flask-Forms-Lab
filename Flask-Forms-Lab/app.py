from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST']) 
def login():
	if request.method == 'GET':
  		return render_template('login.html')
	else:
		if username == request.form['username'] and password == request.form['password']:
			return render_template('home.html', friends = facebook_friends)
		else:
			return "no"
  

@app.route('/friend_exists/<string:friend>') 
def friend_exists(friend):
	is_friend = friend in facebook_friends
	return render_template('friend_exists.html',is_friend = is_friend)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)