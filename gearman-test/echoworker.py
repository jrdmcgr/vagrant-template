import gearman


def echo(gearman_worker, gearman_job):
    return gearman_job.data[::-1]

worker = gearman.GearmanWorker(['127.0.0.1:4730'])
worker.set_client_id('testclient')
worker.register_task('echo', echo)
worker.work()
