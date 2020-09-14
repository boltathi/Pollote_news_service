from mongoengine import Document, StringField, ListField


class category(Document):
    categoryname = StringField

