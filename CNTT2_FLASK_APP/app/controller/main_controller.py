from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response,Flask,send_file
from app import app
from app.service.elastic import es
from app.service.haystack import cv_search_haystack

@app.route("/",methods=['GET'])
def home():
    return render_template("search_page.html")

@app.route("/searchCV",methods=['POST'])
def search_cv():
    searFil = request.json['searchFilter']
    searVal = request.json['searchVal']
    body = {
    "from":0,
    "size":100,
    "query": {
        "bool": {
          "should": [
            {
              "match": {
                searFil: searVal
                }
            }
            ]
            }
        }
    }
    res = es.search(index="cv", body=body)
    print(res)
    return make_response(jsonify({"res":res['hits']['hits']}))

@app.route("/searchCvAdvance",methods=['POST'])
def search_advance():
    # searchVals = request.json['searchDict']
    conditions = []
    for key in request.json.keys():
        conditions.append({"match":{key:request.json[key]}})
    body = {
    "from":0,
    "size":100,
    "query": {
        "bool": {
          "should": conditions
            }
        }
    }
    res = es.search(index="cv", body=body)
    print(res)
    return make_response(jsonify({"res":res['hits']['hits']}))


@app.route("/haystack",methods=['GET','POST'])
def haystack_search():
    query = "sinh viên"
    try:
       query = request.json['haystackData']
    except:
        print("haystackData null")
    res = cv_search_haystack.search_cv(query)
    return make_response(jsonify({'status':200,'result':res}))
    
import os
@app.route('/download/<filename>',methods=['GET','POST'])
def download_file(filename):
    current_dir = os.getcwd()
    # path = request.json['filename']
    # path = os.path.join(os.getcwdb(), "\\CV_PDF\\"+filename)
    return send_file(app.root_path +"\\CV_PDF\\"+filename, as_attachment=True)

