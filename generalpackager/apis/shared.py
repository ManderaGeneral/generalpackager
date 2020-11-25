
from generallibrary import attributes


class _API:
    def get_api_attrs(self):
        """ Get a dict of class variables defined by this api, default value is `None`. """
        return attributes(self, methods=False, properties=False, from_instance=False, from_bases=False)
