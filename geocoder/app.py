import os
import sys

import falcon

from .resources.geocode.Geocode import Geocode
from .clients.HEREGeocoderClient import HEREGeocoderClient
from .clients.GoogleGeocoderClient import GoogleGeocoderClient
from .clients.MemoryCachedClient import MemoryCachedClient

api = application = falcon.API()

requiredEnvVars = ["API_KEY_GOOGLE_GEOCODING",
                   "API_HERE_APP_CODE", "API_HERE_APP_ID"]

try:
    for requiredEnvVar in requiredEnvVars:
        os.environ[requiredEnvVar]
except KeyError:
    print "Please set the environment variables: " + " ".join(requiredEnvVars)
    sys.exit(1)

clients = [
    GoogleGeocoderClient(os.environ["API_KEY_GOOGLE_GEOCODING"]),
    HEREGeocoderClient(os.environ["API_HERE_APP_ID"],
                       os.environ['API_HERE_APP_CODE'])
]

api.add_route('/v1/geocode/json', Geocode([MemoryCachedClient(clients)]))
