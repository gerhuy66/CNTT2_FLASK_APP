from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask
from app import app
from app.service.elastic import es
@app.route("/",methods=['GET'])
def home():

    return render_template("search_page.html")

from app.service.selenium.timeviec_com import crawl_timviec
@app.route("/crawl",methods=['GET'])
def crawl():
    crawl_timviec()
    return make_response(jsonify("status",200))





@app.route("/searchCV",methods=['POST'])
def search_cv():
    searFil = request.json['searchFilter']
    searVal = request.json['searchVal']
    body = {
    "from":0,
    "size":6,
    "query": {
        "match": {
            searFil:searVal
        }
    }
    }
    res = es.search(index="cv", body=body)
    print(res)
    return make_response(jsonify({"res":res['hits']['hits']}))