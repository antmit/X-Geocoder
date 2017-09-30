from .GeocoderClientBase import GeocoderClientBase
import requests


class HEREGeocoderClient(GeocoderClientBase):
    def __init__(self, appId, appCode, uri="https://geocoder.cit.api.here.com/6.2/geocode.json"):
        """A type of GeocoderClient that fetches data from HERE's geocoder API.

        It takes the first result from the list of possible matches

        Attributes:
            appId: The appId for HERE's Geocoder API
            appCode: The appCode for HERE's Geocoder API
            uri: HERE's Geocoder API uri
        """
        self.uri = uri
        self.appId = appId
        self.appCode = appCode

    def getGeocode(self, address):
        """See GeocoderClientBase
        """
        payload = {
            'app_id': self.appId,
            'app_code': self.appCode,
            'searchtext': address
        }
        try:
            r = requests.get(self.uri, params=payload)
            rJson = r.json()

            # TODO: NavigationPosition vs DisplayPosition
            # TODO: NavigationPosition is a list?

            navigationPosition = self.pickBestNavigationPosition(
                rJson["Response"]["View"][0]["Result"])
            return {
                'lat': navigationPosition["Latitude"],
                'lng': navigationPosition["Longitude"]
            }
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def pickBestNavigationPosition(self, results):
        """Determines the best navigation position out of a list of results

        Args:
            results: A JSON object containing a list of results from the HERE geocode API

        Returns:
            a dict containing the keys Latitude and Longitude
        """
        # TODO: Use the MatchQuality instead of picking just the first one.
        return results[0]["Location"]["NavigationPosition"][0]
