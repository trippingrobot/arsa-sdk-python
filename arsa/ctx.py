class _AppCtxGlobals(object):

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

class RequestContext(object):

    def __init__(self, request):
        self.request = request
        self.g = _AppCtxGlobals()
