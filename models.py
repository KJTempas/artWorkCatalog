from peewee import *
import database_config 
db = SqliteDatabase(database_config.database_path) #creating an instance of a database
#creating an instance of a database
#check and remove later
print('THE DATABASE USED IS ' + database_config.database_path)

class Artist(Model):
    name = CharField(unique=True) #fields in artist table
    #how/where to add NOCASE
    email = CharField(unique=True)

    #link this model to art dbase
    class Meta:
        database = db

    def __str__(self):
        return f'Artist ID: {self.id}, Name: {self.name} Email: {self.email}'


class Artwork(Model):
    artist = ForeignKeyField(Artist, backref='artworks')  # add this? -field = Artist.name,
    #artwork id will be generated, since no primary key is specified
    name = CharField(unique=True)   
    price = DecimalField(9,2)
    #price = DecimalField(constraints=[Check('price < 10000')])
    is_available = BooleanField(default=True)

    class Meta:
        database = db
       # constraints = [SQL('UNIQUE ( name COLLATE NOCASE, artist COLLATE NOCASE)')]
    
    def __str__(self):
        return f'{self.name} by {self.artist.name} is available -{self.is_available} for ${self.price}'

#connect to DB and create tables that map to models Artist and Artwork
db.connect()
db.create_tables([Artist, Artwork])