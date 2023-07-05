from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from fab import get_os_version

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hey, we have Flask in a Docker container!"


@app.route('/os_version', methods=['POST', 'GET'])
def os_version():
    if request.method == 'POST':
        gateway = request.form['gateway']
        host_string = request.form['host_string']
        user = request.form['user']
        password = request.form['password']
    else:
        gateway = request.args.get('gateway')
        host_string = request.args.get('host_string')
        user = request.args.get('user')
        password = request.args.get('password')

    passwords = {}
    passwords["192.168.0.10"] = "passwd"
    os_version = get_os_version(gateway, host_string, user, password, passwords)
    data = {'os_version': os_version}
    return jsonify(data)

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
