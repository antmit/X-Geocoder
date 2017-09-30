import json
import falcon


class Geocode(object):
    def __init__(self, clients):
        self.clients = clients

    def on_get(self, req, resp):
        try:
            req.params["address"]

            query = '+'.join(req.params['address'])

            result = None
            for client in self.clients:
                result = client.getGeocode(query)

                if result:
                    break

            if result is None:
                resp.status = falcon.HTTP_500
                return

            doc = {
                'address': query,
                'lat': result['lat'],
                'lng': result['lng']
            }

            # Create a JSON representation of the resource
            resp.body = json.dumps(doc, ensure_ascii=False)

            # The following line can be omitted because 200 is the default
            # status returned by the framework, but it is included here to
            # illustrate how this may be overridden as needed.
            resp.status = falcon.HTTP_200
        except KeyError:
            resp.status = falcon.HTTP_422
