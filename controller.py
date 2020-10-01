import database 
from database import ArtError
import ui
from models import Artist, Artwork
from peewee import *

def add_artist():
    name = ui.get_string('Enter name of artist - First Last')
    name = name.title()
    email = ui.get_string(f'Enter email  for {name}')
    try:
        database.add_artist(name, email)
        print('Added artist')
    except ArtError as e:
        print(e)

def add_artwork():
    name_of_artwork = ui.get_string('Enter name of artwork ') 
    price = ui.get_positive_float('Enter the price for this piece of art ')
    name_of_artist = ui.get_string('Enter name of artist -First Last ')

    artist = database.find_artist(name_of_artist) #get artist object from name provided
    if artist: #if the artist is found/exists
        try:
            database.add_artwork(artist,name_of_artwork, price)
            print('Added artwork')
        except ArtError as e:
            print(e)
    else:
        print('That artist is not on file. Add artist before adding artwork.')

def display_available_work_by_one_artist():
    name_of_artist = ui.get_string('Enter name of artist ')
    artist = database.find_artist(name_of_artist) #retrieve the artist object
    available_artwork = database.display_avail_by_artist(artist) #send that artist to database to retrieve their work
    if available_artwork:
        for row in available_artwork:
            print(row)
    else:
        raise ArtError('There are no available pieces of art by this artist on file')


def show_all_artwork_by_one_artist():
    name_of_artist = ui.get_string('Enter name of artist whose work you would like to see ')
    name = name_of_artist.title()
    artist = database.find_artist(name) #retrieve artist object 

    artwork_by_artist = database.show_artwork_by_one_artist(artist)
    if artwork_by_artist: #if any artwork by that artist is found, print it
        for row in artwork_by_artist:
            print(row)
    else:
        print('There are no pieces of art by this artist on file')    


def change_availability():
    name_of_artwork = ui.get_string('Enter name of artwork to change to Not available/Sold  ')
    artwork = get_artwork_by_name(name_of_artwork)#get the artwork object
    print(artwork) # I can see True go to False here after changing an artwork
    #print(artwork.is_available) #should print True or False - but is not
    database.change_availability(artwork) #send to db to change availability to False
    #print('Changed availability')
    #else:
     #   print('That artwork is already sold')
    

def delete_artwork():
    name_of_artwork = ui.get_string('Enter name of artwork to delete')
    try:
        database.delete_artwork(name_of_artwork) #send to database to delete that artowrk
        print('Deleted artwork')
    except ArtError as e:
        print(e)
    
def show_all_artists():
    artists = database.show_all_artists()
    for artist in artists:
        print(artist)


def show_all_artwork():
    artworks = database.show_all_artwork()
    for artwork in artworks:
        print(artwork)


def get_artwork_by_name(name_of_artwork):
    return Artwork.get_or_none(Artwork.name_of_artwork == name_of_artwork)


def get_artist_by_name():
    name = ui.get_string('Enter name of artist')
    artist = database.find_artist(name)
    if artist:
        print(artist)
    else:
        raise ArtError('That artist is not in the database')
   
def quit_program():
    ui.message('Thanks and bye!')
    


