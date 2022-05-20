from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route('/tarjeta')
def index():
	return render_template('tarjeta.html')

@app.route("/mobile")
def mobile():
	return render_template("mobile.html")

@app.route('/')
def tarjeta():
	return render_template('index.html')


app.static_folder = 'static'
