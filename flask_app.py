from flask import Flask, Response, render_template, send_from_directory

import redis

app = Flask(__name__)

def event_stream():
    r = redis.StrictRedis('localhost')
    p = r.pubsub()
    p.subscribe('test')
    for message in p.listen():
        print message
        yield 'data: %s\n\n' % message['data']

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def hello_word():
    return 'Hello World'

@app.route('/basic')
def sample_html():
    return render_template("basic.html")

@app.route('/redraw')
def sample_html2():
    return render_template("redraw.html")

@app.route('/stream')
def hello_redis():
    return Response(event_stream(),mimetype="text/event-stream")

@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files',path)

@app.route('/shutdown')
def shutdown_server():
    shutdown_server() #<===does't work.
    return 'Server shutting down...'

if __name__=='__main__':
    app.debug = True
    app.run(threaded=True,host='0.0.0.0')
