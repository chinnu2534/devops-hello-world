from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # We include the hostname to show that code is running inside a container
    hostname = socket.gethostname()
    return f"<h1>Hello, DevOps World!</h1><p>Served from container: <b>{hostname}</b></p>"

if __name__ == "__main__":
    # host='0.0.0.0' is crucial for running inside Docker
    app.run(host='0.0.0.0', port=5000)