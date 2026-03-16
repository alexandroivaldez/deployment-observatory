import os
import json
import time
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'version':     os.environ.get('APP_VERSION', 'v0.0.1'),
        'commit':      os.environ.get('GIT_COMMIT',  'local'),
        'branch':      os.environ.get('GIT_BRANCH',  'main'),
        'built_at':    os.environ.get('BUILD_TIME',  'unknown'),
        'deployed_by': os.environ.get('DEPLOYED_BY', 'alexandroivaldez'),
        'hostname':    os.environ.get('HOSTNAME',    'localhost'),
        'region':      os.environ.get('AWS_REGION',  'local'),
    }
    return render_template('index.html', **data)


@app.route('/stream')
def stream():
    def event_stream():
        while True:
            payload = {
                'version': os.environ.get('APP_VERSION', 'v0.0.1'),
                'commit':  os.environ.get('GIT_COMMIT',  'local'),
                'status':  'healthy',
                'ts':      int(time.time()),
            }
            yield f"data: {json.dumps(payload)}\n\n"
            time.sleep(5)

    return Response(event_stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)