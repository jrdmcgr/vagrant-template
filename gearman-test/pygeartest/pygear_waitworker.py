import time
import pygear
import traceback
from serialization import noop_serializer


def log(msg):
    print(msg)


def wait(job):
    try:
        # job.set_serializer(noop_serializer())
        limit = int(job.workload())
        print(job.handle())
        print(job.unique())
        for i in range(limit):
            time.sleep(1)
            job.send_status(i, limit)
        return 'I am finished!\n\n'
    except:
        traceback.print_exc()


worker = pygear.Worker()

worker.set_serializer(noop_serializer())
worker.set_log_fn(log, pygear.PYGEAR_VERBOSE_DEBUG)

worker.add_server('127.0.0.1', 4730)
worker.add_function('wait', 0, wait)

while True:
    worker.work()
