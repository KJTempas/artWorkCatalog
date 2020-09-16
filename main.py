

def main():
    menu = creat_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice.upper() == 'Q':
            break

def creat_menu():
    menu = Menu()
    menu.add_option('1', 'Add New Artist', add_artist)
    menu.add_option('2', 'Add Artwork', add_artwork)
