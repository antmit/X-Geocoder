from .GeocoderClientBase import GeocoderClientBase
import requests


class GoogleGeocoderClient(GeocoderClientBase):
    def __init__(self, apiKey, uri="https://maps.googleapis.com/maps/api/geocode/json"):
        """A type of GeocoderClient that fetches data from Google's geocoder API.

        It takes the first result from the list of possible matches

        Attributes:
            apiKey: An API key for Google's Geocoder API
            uri: The Google Geocoder API uri
        """
        self.uri = uri
        self.apiKey = apiKey

    def getGeocode(self, address):
        """See GeocoderClientBase
        """
        payload = {
            'key': self.apiKey,
            'address': address
        }
        try:
            r = requests.get(self.uri, params=payload)
            rJson = r.json()

            location = self.pickBestLocation(rJson["results"])
            return {
                'lat': location["lat"],
                'lng': location["lng"]
            }
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def pickBestLocation(self, results):
        """Determines the best navigation position out of a list of results

        Args:
            results: A JSON object containing a list of results from the Google geocoder API

        Returns:
            a dict containing the keys lat and lng
        """
        # TODO: Do something better than pick the first one that comes back?
        return results[0]["geometry"]["location"]
