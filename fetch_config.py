import yaml
import pymongo
from importlib import import_module

try:
    with open('config.yml') as config_file:
        config = yaml.safe_load(config_file)
    json_file_path = config['credentials_path']
    lock_limit = config['lock_limit']
    url=config['mongo_url']
    source=config['data_source']
    client=pymongo.MongoClient(url)
except(FileNotFoundError):
    print("cofig.yml file not found.")

if source == "json":
    class_obj= import_module("json_file").Json
if source == "mongo":
    class_obj = import_module("mongo").Mongo

