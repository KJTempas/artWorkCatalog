from peewee import *
from models import Artist, Artwork


def add_artist(name, email):
    try:
        Artist(name = name, email = email).save()
    except IntegrityError as e:
        raise ArtError('Error adding artist because ' + str(e))


def add_artwork(artist, name_of_artwork, price):
    try:
        Artwork(artist = artist, name_of_artwork = name_of_artwork, price = price).save()
    except IntegrityError as e:
        raise ArtError('Error adding artwork because ' + str(e))


def show_artwork_by_one_artist(artist):
    try: #don't need try/except because not modifying dbase
        #artwork_by_artist = Artwork.select().where(Artwork.artist == artist.id) 
        artwork_by_artist = Artwork.select().where(Artwork.artist == artist) 
        return list(artwork_by_artist)
    except ArtError as e:
        print(e)


def change_availability(artwork):
    rows_updated = Artwork.update(is_available = False).where(Artwork.name_of_artwork == artwork.name_of_artwork).execute()
    if not rows_updated:
        raise ArtError('Artwork is already sold')


def display_avail_by_artist(artist):
    try:
        available_artwork = Artwork.select().where(Artwork.artist == artist) and (Artwork.is_available == True)    
        return list(available_artwork)
    except ArtError as e:
        print(e)


def delete_artwork(name_of_artwork):
    try:
        rows_deleted = Artwork.delete().where(Artwork.name_of_artwork == name_of_artwork).execute()
        if not rows_deleted:
            raise ArtError('Tried to delete artwork that does not exist')
    except ArtError as e:
        print(e)        


def show_all_artists():
    try:
        artists = Artist.select()
        return list(artists)
    except ArtError as e:
        print(e)

def show_all_artwork():
    try:
        artworks = Artwork.select()
        return list(artworks)
    except ArtError as e:
        print(e)

def artist_count():
    #return number of artist in dbase
    num_of_artists = Artist.select().count()
    #return Artist.select().count()
    return num_of_artists

def artwork_search(name_of_artwork):
    #artwork = Artwork.select().where((fn.LOWER(Artwork.name).contains(word.lower())))
    #artwork = Artwork.get_or_none(Artwork.name_of_artwork == name_of_artwork)
    artwork = Artwork.get_or_none(Artwork.name_of_artwork == name_of_artwork)
    #artwork = Artwork.select().where(Artwork.name_of_artwork == name_of_artwork)
    #print(artwork)
    return artwork 

def artwork_check_avail_status(name_of_artwork):
    return Artwork.get(Artwork.name_of_artwork == name_of_artwork).is_available

def check_availability(name_of_artwork):
    return Artwork.select(Artwork.is_available).where(Artwork.name_of_artwork == name_of_artwork) 
    #return availability
#below from readlinglist/bookstore
#query = Book.select().where( ( fn.LOWER(Book.title).contains(term.lower() ) ) | (fn.LOWER(Book.author).contains(term.lower())))
#   return list(query)
def find_artist(name_of_artist):
    artist = Artist.get_or_none(Artist.name == name_of_artist)
    #artist = Artist.select().where(Artist.name==name)
    return artist

def artwork_count_all():
    return Artwork.select().count()

def get_artwork_by_id(artwork_id):
    return Artwork.get_or_none(Artwork.id == artwork_id)

class ArtError(Exception):
    pass