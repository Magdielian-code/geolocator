from geoip2.errors import AddressNotFoundError

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
