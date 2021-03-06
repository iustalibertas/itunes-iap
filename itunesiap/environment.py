
__all__ = ('Environment', 'default', 'production', 'sandbox', 'review', 'current')

from .request import Request

class Environment(object):
    """Environement provides option preset for `Request`. `default` is default"""

    ITEMS = ('use_production', 'use_sandbox')

    def __init__(self, **kwargs):
        self.use_production = kwargs.get('use_production', True)
        self.use_sandbox = kwargs.get('use_sandbox', False)
        self.verify_ssl = kwargs.get('verify_ssl', True)

    def clone(self, **kwargs):
        options = self.extract()
        options.update(**kwargs)
        return self.__class__(**options)

    def override(self, **kwargs):
        """Override options in kwargs to given object `self`."""
        for item in self.ITEMS:
            if item in kwargs:
                setattr(self, item, kwargs[item])

    def extract(self):
        """Extract options from `self` and merge to `kwargs` and return new object."""
        options = {}
        for item in self.ITEMS:
            options[item] = getattr(self, item)
        return options

    def verify(self, receipt_data, password=None, proxy_url=None, **kwargs):
        return Request(receipt_data, password, proxy_url).verify(self, **kwargs)

default = Environment(use_production=True, use_sandbox=False, verify_ssl=True)
production = Environment(use_production=True, use_sandbox=False, verify_ssl=True)
sandbox = Environment(use_production=False, use_sandbox=True, verify_ssl=True)
review = Environment(use_production=True, use_sandbox=True, verify_ssl=True)

unsafe = Environment(use_production=True, use_sandbox=True, verify_ssl=False)
