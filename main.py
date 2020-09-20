import controller
import ui

def main():

    while True:
        choice = ui.menu_choice()#get choice from ui
        if choice == '1':
            controller.add_artist()
        elif choice == '2':
            controller.add_artwork()
        elif choice == '3':
            controller.display_all_available_by_artist()
        elif choice == '7':
            break



if __name__== '__main__':
    main()