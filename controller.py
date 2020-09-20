import database 
from database import ArtError
import ui

def add_artist():
    name = ui.get_string('Enter name of artist - Last First')
    email = ui.get_string(f'Enter email  for {name}')
    try:
        database.add_artist(name, email)
        print('Added artist')
    except ArtError as e:
        #art_ui.message('Error: Artist Already on File')
        print(e)

def add_artwork():
    pass


def display_all_available_by_artist():
    name = ui.get_string('Enter name of artist - First Last')
    try: #find the artist, then use the artist.id to get works
        artist = database.find_artist(name)
        print(artist)
        database.display_all_avail_by_artist(artist)
    except ArtError as e:
        print(e)


def show_all_by_one_artist():
    pass

def change_availability():
    pass
    #artwork_id = art_ui.get_artwork_id()
    #artwork = artwork.get_artwork_by_id(artwork_id)


def delete_artwork():
    pass

def quit_program():
    ui.message('Thanks and bye!')



class Artist:
    """represents one artist"""

    def __init__(self, name, email):
        self.name = name
        self.email = email