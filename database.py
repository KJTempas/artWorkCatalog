from peewee import *
from models import Artist, Artwork

#db = SqliteDatabase('artworks.sqlite')

def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))

def find_artist(name):
    try:
        artist = Artist.get_or_none(Artist.name =='name')
        return artist
    except IntegrityError as e:
        raise ArtError('That artist is not in the database' + str(e))

def display_all_avail_by_artist(artist):
    try: #go to artwork table and select those where artist id is same as provided and availability is true
        artworks = Artwork.select(). where (Artwork.artist.id = artist.id) and (Artwork.available == True)
        print(f'These pieces of art by {artist.name} are available: ')
        for artwork in artworks:
            print(artwork)


class ArtError(Exception):
    pass