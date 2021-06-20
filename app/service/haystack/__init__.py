from os import path
from haystack.reader.farm import FARMReader
from app import app
from flask_s3 import FlaskS3
import boto3
import flask
elastic_host = "localhost"
# path = app.root_path+"\\service\\haystack\\bert-multi-cased-finetuned-xquadv1"
# print(path)

farm_reader = FARMReader(model_name_or_path ='mrm8488/bert-multi-cased-finetuned-xquadv1')
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore

document_store = ElasticsearchDocumentStore(host="search-cv-elastic-search-hikqqjksauppdjpqae7ruho2pa.ap-southeast-1.es.amazonaws.com",port=443, username="duchuy1096", password="Metrohuy1770!", scheme='https',index="document",embedding_field=None)