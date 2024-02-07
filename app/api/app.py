from flask import Flask, Blueprint, send_from_directory

api = Blueprint('starter', __name__, static_folder='../react-app/build', static_url_path='')

@api.route('/')
def serve():
    return send_from_directory(api.static_folder, 'index.html')



if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api)
    app.run(host='0.0.0.0')
