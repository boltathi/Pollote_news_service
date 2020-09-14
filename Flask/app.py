from flask import Flask
from mongoengine import connect

from Flask.routes.news import news_api
from Flask.routes.categories import categories_api

from Flask.database import PyMongoDB
from Flask.config import Configuration
from Flask.newsactions.scheduler import startScheduler


from mongoengine import connect




def create_app():
    app = Flask(__name__)
    app.register_blueprint(news_api, url_prefix='/api')
    app.register_blueprint(categories_api, url_prefix='/api')
    return app


if __name__ == '__main__':
    Configuration.initConfig('PROD')
    app = create_app()
    PyMongoDB.setDBConnection(Configuration.getProperty('host'),Configuration.getProperty('port'))
    startScheduler()
    # conn = connect(db='myDB',host='127.0.0.1',port=27017)

    app.run(debug=True)

