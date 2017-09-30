from abc import ABCMeta, abstractmethod


class GeocoderClientBase():
    __metaclass__ = ABCMeta

    @abstractmethod
    def getGeocode(self, address):
        pass
