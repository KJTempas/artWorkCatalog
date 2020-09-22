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
    name = ui.get_string('Enter name of artwork: ')
    price = ui.get_positive_float('Enter the price for this piece of art: ')
    artist = ui.get_string('Enter name of artist -First Last: ')

    try:
        database.add_artwork(name, price, artist)
        print('Added artwork')
    except ArtError as e:
        print(e)


def display_available_work_by_an_artist():
    pass


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
    


