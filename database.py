from peewee import *
from models import Artist, Artwork

#db = SqliteDatabase('artworks.sqlite')

def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
       # new_id =    lastrowid
        #artist.id=new_id
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))


def add_artwork(name, price, artist):
    try:
        Artwork.create(artist = artist, name = name, price = price)
    except ArtError as e:
        print(e)

def show_artwork_by_one_artist(artist):
    try:
        artworks = Artwork.select().where(Artist.id == artist.id)
        return artworks
        #return Artwork.get_or_none(Artist.id == artist_id)
    except ArtError as e:
        print(e)


def change_availability(artwork):
    rows_updated = Artwork.update(is_available = False).where(Artwork.name == artwork.name).execute()
    if not rows_updated:
        raise ArtError('Artwork is already sold')


def delete_artwork(artwork):
    rows_deleted = Artwork.delete().where (Artwork.name == artwork.name).execute()
    if not rows_deleted:
        raise ArtError('Tried to delete artwork that does not exist')

class ArtError(Exception):
    pass