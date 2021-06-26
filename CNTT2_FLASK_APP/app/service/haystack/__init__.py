from os import path
from haystack.reader.farm import FARMReader
from app import app as app_context
# from flask_s3 import FlaskS3
# import boto3
# import flask
# elastic_host = "localhost"
model_path = app_context.root_path+"\\service\\haystack\\bert-multi-cased-finetuned-xquadv1"
print(model_path)
#test thoi
farm_reader = FARMReader(model_name_or_path = model_path,use_gpu=False,num_processes=1)
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore

document_store = ElasticsearchDocumentStore(host="search-cv-elastic-search-hikqqjksauppdjpqae7ruho2pa.ap-southeast-1.es.amazonaws.com",port=443, username="duchuy1096", password="Metrohuy1770!", scheme='https',index="document",embedding_field=None)