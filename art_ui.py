from artwork import Artist




def get_artist_info():
    name = input('Enter the name of the artist in this format - Last, First:  ')
    email = input('Enter artist email:  ')
    #create and return a new Artist object from name and email
    return Artist(name, email)

def message(msg):
    """ prints a message for the user"""
    print(msg)
