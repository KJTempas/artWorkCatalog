from artwork import Artist, Artwork
#from menu import Menu

import art_ui


def main():
    menu = create_menu()

    while True:
        choice = art_ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice.upper() == 'Q':
            break

def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add New Artist', add_artist)
    menu.add_option('2', 'Add Artwork', add_artwork)
    menu.add_option('3', 'Display available work by an artist', display_available_art_by_an_artist)
    menu.add_option('4', 'Show all work by one artist', show_all_by_one_artist)
    menu.add_option('5', 'Change availability status of artwork', change_availability)
    menu.add_option('6', 'Delete an artwork', delete_artwork)
    menu.add_option('7', 'Quit', quit_program)

    return menu

def add_artist():
    try:
        new_artist = art_ui.get_artist_info() #go to art_ui method and return w/ new Artist object
        new_artist.save()
    except Exception as e:
        art_ui.message('Error: Artist Already on File')

def add_artwork():
    pass


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
    art_ui.message('Thanks and bye!')


if __name__== '__main__':
    main()