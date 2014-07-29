import gearman
import traceback
import fakeimport

worker = gearman.GearmanWorker(['localhost:4730'])
worker.set_client_id('testclient')


def import_data(gearman_worker, gearman_job):
    """Gearman task for fakeimport that sends status updates."""

    def update_job_status(numerator, denominator):
        gearman_worker.send_job_status(gearman_job, numerator, denominator)

    try:
        fakeimport.FakeImport(gearman_job.data, update_job_status)
        return ''
    except Exception:
        traceback.print_exc()


worker.register_task('import_data', import_data)
worker.work()
