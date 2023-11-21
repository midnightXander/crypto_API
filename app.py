import requests
from flask import Flask,jsonify

EXCHANGE_URL = 'https://openexchangerates.org/api/latest.json?app_id=5e51bd24a24a4c70aca29ae882eddb36'
EXCHANGE_PARAMS = {'symbols':'XAF,EUR,GBP'}

exchange_data = requests.get(EXCHANGE_URL,EXCHANGE_PARAMS)

#print(exchange_data.json())
rates = exchange_data.json()['rates']

#filtered_rates = {}
#for currency,rate in rates.items():
#    if currency == 'CAD' or currency == 'ZAR' or currency == 'EUR':
#        filtered_rates[currency] = rate
#print(rates)

WEATHER_URL = 'http://api.weatherstack.com/current?access_key=f2ad8220724ce3e1e9fb7525b472969f'

WEATHER_PARAMS = {'query':'Yaounde'}

weather = requests.get(WEATHER_URL,params = WEATHER_PARAMS)
#print(weather.json()['current']['temperature'])
#print(weather.json())

app = Flask(__name__)

@app.route('/') #create main page of web application
def index():
    return "welcome to xander API" #display text on main page

@app.route('/get',methods=['GET'])
def get():

    exchange_data = requests.get(EXCHANGE_URL,EXCHANGE_PARAMS)
    weather_data = requests.get(WEATHER_URL,params=WEATHER_PARAMS)

    return jsonify({
        'usd_rates': exchange_data.json()['rates'],
        'temperature': weather_data.json()['current']['temperature']

    })
    

if __name__ == '__main__':
    app.run() #run the app   