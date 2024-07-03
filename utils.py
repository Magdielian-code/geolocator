# import requests

# def get_location(ip_address, reader):
#     """Retrieves location data for a given IP address using GeoIP2.

#     Args:
#         ip_address: The IP address for which to get location data.
#         reader: A GeoIP2 database reader object.

#     Returns:
#         A dictionary containing the city name or "Unknown" if not found.
#     """
#     try:
#         response = reader.city(ip_address)
#         city = response.city.names['en']
#     except AddressNotFoundError:
#         city = "Unknown"
#     return {'city': city}


# def get_temperature(city, api_key):
#   """Retrieves temperature data for a given city using ipapi API.

#   Args:
#       city: The city name for which to get temperature data.
#       api_key: Your API key for the ipapi service.

#   Returns:
#       A dictionary containing the temperature in Celsius or None if unsuccessful.
#   """

#   # Replace with the ipapi API endpoint URL for weather data (if available)
#   url = f"https://api.ipapi.com/addr/{city}?apikey={api_key}"

#   try:
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for non-200 status codes
#     data = response.json()
    
#     # Check if temperature data is available in the ipapi response
#     if 'temp' in data:
#         temperature_celsius = data["temp"]
#     else:
#         # Handle the case where temperature data is not available from ipapi
#         print(f"Temperature data not available from ipapi for {city}")
#         return None  # Or return a default value

#     return {"temperature": temperature_celsius}
#   except requests.exceptions.RequestException as e:
#     print(f"Error retrieving temperature: {e}")
#     return None
