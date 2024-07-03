import requests

def get_location(ip_address):
  """Retrieves location data for a given IP address using ipapi.

  Args:
      ip_address: The IP address for which to get location data.

  Returns:
      A dictionary containing the city name or "Unknown" if not found.
  """
  url = f"https://ipapi.co/{ip_address}/json/"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    city = data.get("city", "Unknown") 
  except requests.exceptions.RequestException as e:
    print(f"Error fetching location: {e}")
    city = "Unknown"
  return {"city": city}


def get_temperature(ip_address):
  """Retrieves temperature data for a given city (replace with actual weather API call if ipapi doesn't provide it).

  Args:
      city: The city name for which to get temperature data.
      api_key: Your API key for the weather service (if applicable).

  Returns:
      A dictionary containing the temperature or None if unsuccessful.
  """

  WEATHER_API_KEY = '9d08841fb334f501656cf35139431582'
  url = f"https://ipapi.co/{ip_address}/json/"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()


    # Get longitude and latitude
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}'
     
    temperature = requests.get(weather_url)
    temperature = temperature.json()
    temperature = temperature['main']['temp']


    return temperature
  
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving temperature: {e}")
    return None
