import logging
import time
import gearman

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')


def wait(worker, job):
    logging.info('Working on job: %s', job.handle)
    try:
        limit = int(job.data)
        for i in range(limit):
            time.sleep(1)
            worker.send_job_status(job, i, limit)
        return 'SUCCESS'
    except:
        logging.exception('FAIL')
        raise


if __name__ == '__main__':
    worker = gearman.GearmanWorker(['127.0.0.1:4730'])
    worker.register_task('wait', wait)
    worker.work()
