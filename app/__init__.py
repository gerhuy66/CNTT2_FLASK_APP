import flask
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask


app = Flask(__name__,static_url_path='/static')



from app.controller import main_controller