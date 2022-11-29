from flask import Flask

app = Flask(__name__, static_folder='app', static_url_path='')


@app.route('/')
def galaxy():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(threaded=True, port=8080)