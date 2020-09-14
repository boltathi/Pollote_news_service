import time
import atexit
from Flask.database import PyMongoDB
import json
import time
from Flask.newsactions.fetchnewsApiService import FetchNewsApi
from apscheduler.schedulers.background import BackgroundScheduler


# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def startScheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=updateNewsWithJob, trigger="interval", hours=5)
    scheduler.start()



def updateNewsWithJob():
    try:
        js = PyMongoDB.getAllData('category')[0]
        for categories in js['categoriesList']:
            subcategories = categories['subcategory']
            category = categories['category']
            for subcategory in subcategories:

                news = json.loads(FetchNewsApi.getNews(subcategory))['news']
                print(news)
                PyMongoDB.updateData('news', 'news', news, 'subcategory', subcategory, 'category', category)
                time.sleep(120)
        print("**************")
        return json.dumps({"message": "successfully updated", "success": True})
    except Exception as e:
        print("Exception:"+str(e))
        return json.dumps({"message":"Failed to update","success":False})