from mongoengine import connect, Document, StringField, ListField, CASCADE, ReferenceField

connect(host='mongodb+srv://mydb:bumegalol@matz.2ewqgqh.mongodb.net/?retryWrites=true&w=majority')


class Author(Document):
    fullname = StringField(required=True)
    date_born = StringField()
    born_location = StringField()
    bio = StringField()


class Quotes(Document):
    author = ReferenceField(Author)
    tags = ListField(StringField())
    quote = StringField(required=True)
