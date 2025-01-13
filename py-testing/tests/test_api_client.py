import unittest
from src.api_client import get_location
from unittest.mock  import patch

class ApiClientTests(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "Mexico",
            "regionName": "Guanajuato",
            "cityName": "Leon",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "Mexico")
        self.assertEqual(result.get("region"), "Guanajuato")
        self.assertEqual(result.get("city"), "Leon")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")