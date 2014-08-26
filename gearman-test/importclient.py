import gearman
from statusbar import status_bar
from importdata import DATA


def print_request_status(job_request):
    if job_request.complete:
        print("Job %s finished!  Result: %s - %s"
              % (job_request.job.unique, job_request.state, job_request.result))
    elif job_request.timed_out:
        print("Job %s timed out!" % job_request.unique)
    elif job_request.state == gearman.job.UNKNOWN:
        print("Job %s failed!" % job_request.unique)


if __name__ == '__main__':
    client = gearman.GearmanClient(['127.0.0.1:4730'])
    request = client.submit_job('import_data', DATA, wait_until_complete=False)
    print(request.job.handle)
    while not request.complete:
        request = client.get_job_status(request)
        status_bar(request.status.get('numerator', 0),
                   request.status.get('denominator', 0))

    print_request_status(request)
