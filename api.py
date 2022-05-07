from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/hit',methods=['GET'])
def predict():
	return jsonify( 
		result = "This is my own api 😍"
	)
    