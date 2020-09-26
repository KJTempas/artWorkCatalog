import re

def menu_choice():
    while True:
        print("""
1 to add Artist
2 to add Artwork
3 to change Availability to Sold
4 to show all Artwork by one Artist
5 to display all Available Artwork by one Artist
6 to delete Artwork
7 to show all Artists
8 to quit
       """)
        response = get_string('Enter choice? ')
        if response in ['1','2','3','4','5','6','7', '8']:
            return response
        print('Invalid choice.  Please select one of the options.')



def get_string(question, max_length=None):
    while True:
        response = input(f'{question}: ')
        if response: #blank string not allowed
            return response
        print('Empty responses are not allowed. Please enter a string. ')

def get_positive_float(question):
    while True:
        try:
            response = float(input(f'{question}: '))
            if response >=0:
                return response
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter a number')

def get_email(question):
    while True:
        response = input(f'{question}:')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  #https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        if (re.search(regex,response)):#if the response conforms to the regex pattern for email
            return response
        print('Please enter a valid email address')


def message(msg):
 #   """ prints a message for the user"""
    print(msg)
