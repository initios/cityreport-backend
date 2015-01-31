from pygeocoder import Geocoder


def reverse_geocode(lat, lon):
    results = Geocoder.reverse_geocode(lat, lon)

    data = {
        'postal_code': results.postal_code,
        'city': results.city,
        'state': results.state,
        'county': results.county,
        'country': results.country,
        'address': results.address or '',
    }

    return data
