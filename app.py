from flask import Flask, request, jsonify
import geoip2.database

app = Flask(__name__)

# Replace 'path/to/GeoLite2-City.mmdb' with the actual path to your GeoIP2 database
reader = geoip2.database.Reader('Home/Downloads/GeoLite2-City_20240628/GeoLite2-City.mmdb')

@app.route('/api/hello', methods=['GET'])
def hello():
  visitor_name = request.args.get('visitor_name')
  visitor_ip = request.remote_addr

  # Using GeoIP2 to get location data (replace with your free API if needed)
  try:
      response = reader.city(visitor_ip)
      city = response.city.names['en']
  except geoip2.errors.AddressNotFoundError:
      city = "Unknown"

  # Assuming a temperature of 11 degrees for demonstration (replace with API call)
  temperature = 11

  greeting = f"Hello, {visitor_name}, the temperature is {temperature} degrees in {city}"
  response = jsonify({'client_ip': visitor_ip, 'location': city, 'greeting': greeting})
  return response

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  # Listen on all interfaces, port 5000
