import sys
from .models import PreferencesUtilsModel

class PrefProcessor(object):
    def __getattr__(self, attr):
        if attr == '__file__':
            # autoreload support in dev server
            return __file__
        else:
            return lambda request: {attr: PreferencesUtilsModel.__subclasses__[attr].instance()}

sys.modules[__name__ + '.preferences'] = PrefProcessor()
