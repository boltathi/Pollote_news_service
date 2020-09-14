import flask
from flask import Blueprint, jsonify

from Flask.database import PyMongoDB

categories_api = Blueprint('categories', __name__)



@categories_api.route('/getcategories', methods=['GET'])
def getcategories():
    try:

        js=PyMongoDB.getAllData('category')[0]
        # for jsnew in js['categoriesList']:
        #     subcategory=jsnew['subcategory']
        #     category=jsnew['category']
        #     for subcat in subcategory:
        #         print("Category:"+category ,"Subcategory:"+subcat)
        return jsonify({"sucess": True}, {"data": js['categoriesList']})

    except Exception as e:
        return jsonify({"sucess":False},{"message":"Error Occured "+str(e)}), 400



@categories_api.route('/insertcategories', methods=['POST'])
def insertcategories():
    try:
        PyMongoDB.insertData('category', flask.request.json)
        return jsonify({"sucess": True}, {"message": "successfully Inserted"}),200
    except Exception as e:
        return jsonify({"sucess":False},{"message":"Error Occured "+str(e)}), 400

