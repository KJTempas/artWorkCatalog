from peewee import *
from models import Artist, Artwork


def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))


def add_artwork(name, price, artist):
    try:
        Artwork.create(artist = artist, name = name, price = price)
    except IntegrityError as e:
        raise ArtError('Error adding artwork because ' + str(e))

def show_artwork_by_one_artist(artist):
    #print(artist) #works- prints object
    #print(artist.id) #works - prints id of that artist
    try:
        #artworks = Artwork.select().where(Artwork.artist_id.id==artist.id) #no such colum t2.id
        artworks = Artwork.select().where(Artwork.artist_id==artist.id) #there are no pieces of art by this artist on file
        

        return artworks
        #return Artwork.get_or_none(Artist.id == artist_id)
    except ArtError as e:
        print(e)


def change_availability(artwork):
    rows_updated = Artwork.update(is_available = False).where(Artwork.name == artwork.name).execute()
    if not rows_updated:
        raise ArtError('Artwork is already sold')

def display_avail_by_artist(artist):
    try:
       # artworks = Artwork.select().where(artist.id==artist) and (Artwork.is_available == True) #artist_id is not defined
        artworks = Artwork.select().where(Artwork.artist_id==artist.id) and (Artwork.is_available == True) #same error as above
        #artworks = Artwork.select().where(Artwork.artist_id==artist.id) and (Artwork.is_available == True)
        #artworks = Artwork.select().where(Artwork.artist_id==artist.id) and (Artwork.is_available == True)
        #artworks = Artwork.select().where(Artwork.artist_id==artist.id) and (Artwork.is_available == True)
        #artworks = Artwork.select().where(Artwork.artist_id==artist.id) and (Artwork.is_available == True)
        return artworks
    except ArtError as e:
        print(e)

def delete_artwork(artwork):
    rows_deleted = Artwork.delete().where (Artwork.name == artwork.name).execute()
    if not rows_deleted:
        raise ArtError('Tried to delete artwork that does not exist')

def artist_count():
    #return number of artist in dbase
    num_of_artists = Artist.select().count()
    #return Artist.select().count()
    return num_of_artists

def artwork_count_all():
    return Artwork.select().count()

class ArtError(Exception):
    pass