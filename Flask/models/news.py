from mongoengine import Document, StringField, ListField


class news(Document):
    category = StringField()
    subcategory = StringField()
    news = Document
