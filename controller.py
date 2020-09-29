import database 
from database import ArtError
import ui
from models import Artist, Artwork
from peewee import *

def add_artist():
    name = ui.get_string('Enter name of artist - First Last')
    name = name.title()
    email = ui.get_string(f'Enter email  for {name}')
    #email = ui.get_email(f'Enter email  for {name}')
    try:
        database.add_artist(name, email)
        print('Added artist')
    except ArtError as e:
        #art_ui.message('Error: Artist Already on File')
        print(e)

def add_artwork():
    name = ui.get_string('Enter name of artwork ')
    name = name.title()
    price = ui.get_positive_float('Enter the price for this piece of art ')
    artist = ui.get_string('Enter name of artist -First Last ')
    artist = artist.title()
    
    try:
        database.add_artwork(name, price, artist)
        print('Added artwork')
    except ArtError as e:
        print(e)


def display_available_work_by_an_artist():
    name = ui.get_string('Enter name of artist ')
    name = name.title()
    artist = get_artist_by_name(name)
    print(artist)
    try:
        available_artwork = database.display_avail_by_artist(artist)
        if available_artwork:
            for row in available_artwork:
                print(row)
        else:
            raise ArtError('There are no available pieces of art by this artist on file')

    except ArtError as e:
        print(e)

def show_all_artwork_by_one_artist():
    name = ui.get_string('Enter name of artist whose work you would like to see ')
    name = name.title()
    artist = get_artist_by_name(name) #retrieve artist object 
    #print(artist)
    #print(artist.id)

    try:
        artwork_by_artist = database.show_artwork_by_one_artist(artist) 
       
        print(artwork_by_artist)
        if artwork_by_artist: #if any artwork by that artist is found
            for row in artwork_by_artist:
                print(row)
        else:
            raise ArtError('There are no pieces of art by this artist on file')
    except ArtError as e:
        print(e)


def change_availability():
    name = ui.get_string('Enter name of artwork to change availability: ')
    name = name.title()
    artwork = get_artwork_by_name(name)
    try:
        database.change_availability(artwork) #send to database to delete that artwork
        print('Changed availability')
    except ArtError as e:
        print(e)
    

def delete_artwork():
    name = ui.get_string('Enter name of artwork to delete')
    name = name.title()
    artwork = get_artwork_by_name(name)
    try:
        database.delete_artwork(artwork) #send to database to delete that artowrk
        print('Deleted artwork')
    except ArtError as e:
        print(e)
    
def show_all_artists():
    artists = database.show_all_artists()
    for artist in artists:
        print(artist)

def search_for_artwork_by_name():
    name = ui.get_string('Enter name of artwork')
    #artwork = database.artwork_search(name)
    artwork = database.artwork_search(name)
    #artwork = Artwork.get_or_none(Artwork.name==name)
    print(artwork)
    #artwork = database.artwork_search(word)
    #print(artwork)


def get_artwork_by_name(name):
    return Artwork.get_or_none(Artwork.name == name)

def get_artist_by_name():
    name = ui.get_string('Enbter name of artist')
    artist = database.find_artist(name)
    #return Artist.get_or_none(Artist.name == name)
    print(artist)
   
def quit_program():
    ui.message('Thanks and bye!')
    


