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
    menu.add_option('3', 'Display available work by one artist', display_available_art)
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
