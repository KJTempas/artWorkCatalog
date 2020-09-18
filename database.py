from peewee import *
from models import Artist, Artwork

#db = SqliteDatabase('artworks.sqlite')

def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))

class ArtError(Exception):
    pass