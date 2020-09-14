import json


import flask
from flask import Blueprint, jsonify, request
from Flask.newsactions.fetchnewsApiService import FetchNewsApi
from Flask.models.news import news
from Flask.database import PyMongoDB
import shed

news_api = Blueprint('news', __name__)


@news_api.route('/updatenews', methods=['GET'])
def update_news_to_db():
    try:
        subcategory=flask.request.args.get('subcategory')
        category=flask.request.args.get('category')
        news_api_response=json.loads(FetchNewsApi.getNews(flask.request.args.get('subcategory')))
        print(news_api_response['message'])
        if news_api_response['message']=='success':
            print(news_api_response['news'])
            PyMongoDB.updateData('news','news',news_api_response['news'],'subcategory',subcategory,'category',category)
            return jsonify({"sucess":True,"message":"sucess"}),200
        else:
            return jsonify(news_api_response),400
    except Exception as e:
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400




@news_api.route('/fetchnews',methods=['GET'])
def fetchNews():
    try:
        news_api_response=json.loads(FetchNewsApi.getNews(flask.request.args.get('subcategory')))
        if news_api_response['message']=='sucess':
            return jsonify(news_api_response),200
        else:
            return jsonify(news_api_response),400
    except Exception as e:
        print(e)
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400


@news_api.route('/getnews',methods=['GET'])
def getnews():
    try:
        subcategory = flask.request.args.get('subcategory')
        data = PyMongoDB.getData('news','subcategory',subcategory)

        return jsonify({"sucess": True}, {"data": data}),200
    except Exception as e:
        return jsonify({"sucess": False}, {"message": "Error Occured " + str(e)}), 400
