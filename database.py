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

#def show_artwork_by_one_artist(artist):#original
def show_artwork_by_one_artist(artist):
    #print(artist) #works- prints object
    #print(artist.id) #works - prints id of that artist

    #try: #don't need try/except because not modifying dbase
        #artwork_by_artist = Artwork.select().where(Artwork.artist == artist.id) 
    artwork_by_artist = Artwork.select().where(Artwork.artist.name == artist.name) 
    return list(artwork_by_artist)
   # except ArtError as e:
       # print(e)


def change_availability(name):
    rows_updated = Artwork.update(is_available = False).where(Artwork.name == name).execute()
    if not rows_updated:
        raise ArtError('Artwork is already sold')

def display_avail_by_artist(artist):
    #try: #not needed since not modifying dbase
    available_artwork = Artwork.select().where(Artwork.artist == artist.id) and (Artwork.is_available == True) #same error as above    
    return list(available_artwork)
    #except ArtError as e:
     #   print(e)

def delete_artwork(name):
    rows_deleted = Artwork.delete().where (Artwork.name == name).execute()
    if not rows_deleted:
        raise ArtError('Tried to delete artwork that does not exist')

def show_all_artists():
    try:
        artists = Artist.select()
        return list(artists)
    except ArtError as e:
        print(e)

def artist_count():
    #return number of artist in dbase
    num_of_artists = Artist.select().count()
    #return Artist.select().count()
    return num_of_artists

def artwork_search(name):
    #artwork = Artwork.select().where((fn.LOWER(Artwork.name).contains(word.lower())))
    #return Artwork.get_or_none(Artwork.name == name)
    #artwork = Artwork.get_or_none(Artwork.name == name)
    artwork = Artwork.select().where(Artwork.name == name)
    return artwork
    

#below from readlinglist/bookstore
#query = Book.select().where( ( fn.LOWER(Book.title).contains(term.lower() ) ) | (fn.LOWER(Book.author).contains(term.lower())))
#   return list(query)
def find_artist(artist.name):
    artist = Artist.get_or_none(Artist.name == name)
    #artist = Artist.select().where(Artist.name==name)
    return artist

def artwork_count_all():
    return Artwork.select().count()

def get_artwork_by_id(artwork_id):
    return Artwork.get_or_none(Artwork.id == artwork_id)

class ArtError(Exception):
    pass