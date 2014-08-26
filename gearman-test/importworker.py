import logging
import gearman
import fakeimport


def import_data(worker, job):
    """Gearman task for fakeimport that sends status updates."""

    def update_job_status(numerator, denominator):
        worker.send_job_status(job, numerator, denominator)

    try:
        logging.info('Importing data... ')
        fakeimport.FakeImport(job.data, update_job_status)
        return '' 
    except Exception:
        logging.exception('FAIL')


if __name__ == '__main__':
    worker = gearman.GearmanWorker(['localhost:4730'])
    worker.set_client_id('importworker')
    worker.register_task('import_data', import_data)
    worker.work()
