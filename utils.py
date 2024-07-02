from geoip2.errors import AddressNotFoundError
import requests

def get_location(ip_address, reader):
    """Retrieves location data for a given IP address using GeoIP2.

    Args:
        ip_address: The IP address for which to get location data.
        reader: A GeoIP2 database reader object.

    Returns:
        A dictionary containing the city name or "Unknown" if not found.
    """
    try:
        response = reader.city(ip_address)
        city = response.city.names['en']
    except AddressNotFoundError:
        city = "Unknown"
    return {'city': city}

import requests

def get_temperature(city, api_key):
  """Retrieves temperature data for a given city using an API.

  Args:
      city: The city name for which to get temperature data.
      api_key: Your API key for the weather service.

  Returns:
      A dictionary containing the temperature in Celsius or None if unsuccessful.
  """

  # Replace with your desired weather API endpoint URL
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    temperature_kelvin = data["main"]["temp"]
    # Convert Kelvin to Celsius (you can adjust the conversion if needed)
    temperature_celsius = round(temperature_kelvin - 273.15, 2)
    return {"temperature": temperature_celsius}
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving temperature: {e}")
    return "11 degress Celcius"
