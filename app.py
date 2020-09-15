from flask import Flask
# from mongoengine import connect

from myservices.routeconfigs.news import news_api
from myservices.routeconfigs.categories import categories_api

from myservices.database import PyMongoDB
from myservices.config import Configuration



app=Flask(__name__)

def set_blue_print():
    # app= Flask(__name__)
    app.register_blueprint(news_api, url_prefix='/news')
    app.register_blueprint(categories_api, url_prefix='/news')
    return app

# @application.before_request
def beforeRequestValidation():
    # resp=requests.get("http://newsapi.org/v2/everything?q=mental health&sortBy=publishedAt&apiKey=19d7070e247441b6910afb5922cc1313")
    print("HERE IT IS")
    # print(resp.status_code)
    #
    # if resp.status_code != 200:
    #     return resp.json()


if __name__ == '__main__':
    Configuration.initConfig('PROD')
    set_blue_print()
    @app.before_request
    def before_calback():
        beforeRequestValidation()

    PyMongoDB.setDBConnection(Configuration.getProperty('host'),Configuration.getProperty('port'))
    # startScheduler()
    # conn = connect(lsdb='myDB',host='127.0.0.1',port=27017)

    app.run(host='127.0.0.1',port=8080,debug=True)

