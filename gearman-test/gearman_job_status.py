import sys
import gearman


def get_job_status(client, job_handle):
    conn = client.connection_list[0]
    client.establish_connection(conn)
    job = gearman.job.GearmanJob(conn, job_handle, None, None, None)
    request = gearman.job.GearmanJobRequest(job)
    request.state = 'CREATED'
    return client.get_job_status(request).status


if __name__ == '__main__':
    job_handle = sys.argv[1]
    client = gearman.GearmanClient(['127.0.0.1'])
    print(get_job_status(client, job_handle))
