from flask import Flask, request, jsonify
import geoip2.database
import os
import utils

app = Flask(__name__)

# Replace 'path/to/GeoLite2-City.mmdb' with the actual path to your GeoIP2 database
reader = geoip2.database.Reader(os.getenv('GEOLITE2_DB_PATH'))

@app.route('/api/hello', methods=['GET'])
def hello():
  visitor_name = request.args.get('visitor_name')
  visitor_ip = request.remote_addr

  location = utils.get_location(visitor_ip, reader)
  city = location['city']

  temperature = utils.get_temperature(city)  # Placeholder function

  greeting = f"Hello, {visitor_name}, the temperature is {temperature} degrees in {city}"
  response = jsonify({'client_ip': visitor_ip, 'location': city, 'greeting': greeting})
  return response

# ...
