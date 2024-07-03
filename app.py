from flask import Flask, request, jsonify
import utils

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
  visitor_name = request.args.get('visitor_name')
  visitor_ip = request.remote_addr
  visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

  location = utils.get_location(visitor_ip)
  city = location['city']

  temperature = utils.get_temperature(visitor_ip)

  greeting = f"Hello, {visitor_name}, the temperature is {temperature} degrees in {city}"
  response = jsonify({'client_ip': visitor_ip, 'location': city, 'greeting': greeting})
  return response
