import pygear
import sys
from serialization import noop_serializer

client = pygear.Client()
client.set_serializer(noop_serializer())
client.add_server('127.0.0.1', 4730)


if __name__ == '__main__':
    status = client.unique_status(sys.argv[1])
    print('status: %s/%s' % (status['numerator'], status['denominator']))
