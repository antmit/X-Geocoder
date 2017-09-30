from .GeocoderClientBase import GeocoderClientBase
import requests


class MemoryCachedClient(GeocoderClientBase):
    def __init__(self, clients):
        """A type of GeocoderClient that caches the results from other GeocoderClients.

        Attributes:
            clients: a list of GeocoderClientBase derived instances
        """
        self.cache = {}
        self.clients = clients

    def normalizeAddress(address):
        """Normalizes an input address.

        Args:
            address: The address

        Returns:
            A normalized address
        """
        return address

    def getGeocode(self, address):
        """Gets a geocode given an addresss

        Checks the in-memory cache of normalized addresses to geocodes.  If not in
        the cache, utilizes clients in priority order to retrieve live data and then
        updates the cache

        Args:
            address: The address

        Returns:
            a dict with the keys lat, lng.

            or None if no client can retrieve a geocode.
        """
        if address in self.cache.keys():
            return self.cache[address]

        for client in self.clients:
            result = client.getGeocode(address)

            if result:
                self.cache[address] = result
                break

        try:
            return self.cache[address]
        except KeyError:
            return None
