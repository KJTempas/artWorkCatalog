from peewee import *

db = SqliteDatabase('art.sqlite') #creating an instance of a database

class Artist(Model):
    name = CharField(unique=True) #fields in artist table
    email = CharField(unique=True)
    #id = IntegerField()  ? but is autoassigned

    #link this model to art dbase
    class Meta:
        database = db

    def __str__(self):
        return f'Artist ID: {self.id}, Name: {self.name} Email: {self.email}'


class Artwork(Model):
    artist = ForeignKeyField(Artist)# , backref='artworks') #not sure about backrefs 
    #artworkid - autoincrement?
    name_of_artwork = CharField()   #unique
    price = DecimalField(9,2)
    is_available = BooleanField(default=True)

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.name_of_artwork} is {self.is_available} available for {self.price}'

#connect to DB and create tables that map to models Artist and Artwork
db.connect()
db.create_tables([Artist, Artwork])