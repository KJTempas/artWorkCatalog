def menu_choice():
    while True:
        print("""
1 to add Artist
2 to add Artwork
3 -to display all artwork by an Artist
7 to quit
       """)
        response = get_string('Enter choice? ')
        if response in ['1','2','3','7']:
            return response
        print('Invalid choice.  Please select one of the options.')



def get_string(question, max_length=None):
    while True:
        response = input(f'{question}: ')
        if response: #blank string not allowed
            return response
        print('Empty responses are not allowed. Please enter a string. ')





#def message(msg):
 #   """ prints a message for the user"""
  #  print(msg)
