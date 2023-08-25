from flask import Flask, render_template, request, jsonify
from weather import get_current_weather
from waitress import serve
import requests
from dotenv import load_dotenv
import os
from pprint import pprint




app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template(
        'index.html'
    )


@app.route('/weather')

def get_weather():
    city            = request.args.get('cityName')
    weather_data    = get_current_weather(city)
    return render_template(
        'weather.html',
        city      =weather_data["name"],
        country   = weather_data["sys"]['country'],
        temp      = weather_data["main"]["temp"],
        desc    = weather_data["weather"][0]['description'].capitalize(),
        feels_like= weather_data['main']['feels_like']
    )


if __name__ == "__main__":
    app.debug = True
    # app.run(host= "0.0.0.0", port= 5050)  this is for developent alone
    serve(app, host= "0.0.0.0", port= 5050) 