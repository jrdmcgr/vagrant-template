class noop_serializer(object):
    def loads(self, string):
        return string

    def dumps(self, other):
        return other