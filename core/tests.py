from django.test import TestCase

from . import services


class ReverseGeocodeTest(TestCase):
    def test_returns_the_location_and_state_for_a_given_coordinates(self):
        expected = {'postal_code': '36204', 'state': 'Galicia', 'city': 'Vigo',
                    'county': 'Pontevedra', 'country': 'Spain'}

        self.assertEqual(expected, services.reverse_geocode(42.228034, -8.719611))
