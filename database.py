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
    print(artist) #works- prints object
    print(artist.id) #works - prints id of that artist

    try:
        artwork_by_artist = Artwork.select().where(Artwork.artist == artist.id) 
        return artwork_by_artist
    except ArtError as e:
        print(e)


def change_availability(artwork):
    rows_updated = Artwork.update(is_available = False).where(Artwork.name == artwork.name).execute()
    if not rows_updated:
        raise ArtError('Artwork is already sold')

def display_avail_by_artist(artist):
    try:
        available_artwork = Artwork.select().where(Artwork.artist == artist.id) and (Artwork.is_available == True) #same error as above
        
        return available_artwork
    except ArtError as e:
        print(e)

def delete_artwork(artwork):
    rows_deleted = Artwork.delete().where (Artwork.name == artwork.name).execute()
    if not rows_deleted:
        raise ArtError('Tried to delete artwork that does not exist')

def show_all_artists():
    try:
        artists = Artist.select()
        return artists
    except ArtError as e:
        print(e)

def artist_count():
    #return number of artist in dbase
    num_of_artists = Artist.select().count()
    #return Artist.select().count()
    return num_of_artists

def artwork_count_all():
    return Artwork.select().count()

class ArtError(Exception):
    pass