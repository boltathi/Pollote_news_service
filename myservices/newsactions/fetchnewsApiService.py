from myservices.config import Configuration
import requests
import json



class FetchNewsApi:

    @classmethod
    def getNews(cls,query):
        try:

            resp = requests.get(Configuration.getProperty("FETCH_NEWS_URI").replace('query',query))

            if resp.status_code != 200:
                return json.dumps({"success":False,"message":"Failed"})
            else:
                return json.dumps({"success": True, "message": "success", "news": resp.json()})


        except Exception as e:
            return json.dumps({"success":False,"message":"Exception "})

