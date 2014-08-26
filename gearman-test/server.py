import flask
import gearman
from gearman_job_status import get_job_status

app = flask.Flask(__name__, static_url_path='')
gm_client = gearman.GearmanClient(['localhost'])


@app.route('/')
def index():
    with open('index.html') as html:
        return html.read()


@app.route('/wait/<int:seconds>')
def wait(seconds):
    job_request = gm_client.submit_job('wait', str(seconds), background=True)
    return job_request.job.handle


@app.route('/job/<job_handle>')
def check_job(job_handle):
    status = get_job_status(gm_client, str(job_handle))
    return flask.jsonify(status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
