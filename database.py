from peewee import *
from models import Artist, Artwork

#db = SqliteDatabase('artworks.sqlite')

def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))


def add_artwork(name, price, artist):
    try:
        #Artwork(name = name, price = price, artist = artist)
        Artwork.create(artist = artist, name = name, price = price)
    except ArtError as e:
        print(e)

class ArtError(Exception):
    pass