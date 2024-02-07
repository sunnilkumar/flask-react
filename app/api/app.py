from flask import Flask, request, jsonify, render_template,send_from_directory, Blueprint
from flask_cors import CORS, cross_origin


api = Blueprint('starter',__name__,static_folder='../react-app/build',static_url_path='')
cors = CORS(api)

@api.route('/')
def serve():
    return send_from_directory(api.static_folder, 'index.html')

