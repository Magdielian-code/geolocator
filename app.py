from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

# Replace 'path/to/GeoLite2-City.mmdb' with the actual path to your GeoIP2 database
WEATHER_API_KEY = '9d08841fb334f501656cf35139431582'

@app.route('/api/hello', methods=['GET'])
def hello():
  visitor_name = request.args.get('visitor_name')
  visitor_ip = request.remote_addr

  location = utils.get_location(visitor_ip,)
  city = location['city']

  temperature = utils.get_temperature(city)  # Uses ipapi now

  greeting = f"Hello, {visitor_name}, the temperature is {temperature} degrees in {city}"
  response = jsonify({'client_ip': visitor_ip, 'location': city, 'greeting': greeting})
  return response
