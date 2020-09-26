from unittest import TestCase
import database_config


#change database path to test_art.sqlite
database_config.database_path = 'test_art.sqlite'

import database

import controller
from models import Artist, Artwork
from database import ArtError, IntegrityError

class TestArtwork(TestCase):
    
    def setUp(self): #supposed to run before every test - but doesn't seem to do it
        # connect to dbase and delete from dbase all data in each table
        Artist.delete().execute() #deletes everything in the table
        Artwork.delete().execute()
        

    def add_test_data(self): #helper/utility method
        self.artist1 = Artist(name = 'Auguste Rodin', email = 'ar@gmail.com')
        self.artist2 = Artist(name = 'Paul Cezanne', email = 'pc@gmail.com')
        self.artist1.save()
        self.artist2.save()
        
        self.artwork1 = Artwork(name = 'The Thinker', price = 500, artist = self.artist1)
        self.artwork1.save()
        self.artwork2 = Artwork(name = 'The Bathers', price =600, artist = self.artist2)
        self.artwork2.save()


    def test_add_artist(self):
        #Artist.delete().execute() #start w empty artist table
        artist = Artist(name = 'Quinn Tempas', email = 'qt@gmail.com')
        artist.save()
        self.assertEqual(1, database.artist_count())
    
    def test_add_artist_not_unique(self):
        #Artist.delete().execute()
        self.add_test_data() #should violate unique constraint for name and/or email
        artist3 = Artist(name = 'Paul Cezanne', email = 'pc@gmail.com') #both name and email not unique
        artist4 = Artist(name = 'Saul Cezanne', email = 'pc@gmail.com') #email not unique
        artist5 = Artist(name = 'Paul Cezanne', email = 'cp@gmail.com') #name not unique
        
        with self.assertRaises(IntegrityError): #should raise an error because name & email not unique
            artist3.save()
            artist4.save()
            artist5.save()

           
    def test_add_artwork(self):
        #Artist.delete().execute()
        #Artwork.delete().execute()
        self.add_test_data() #to make sure artist is in the artist table
        artwork = Artwork(artist = 'Paul Cezanne', name='The Blue Vase', price = 600)
        artwork.save()
        self.assertEqual(3, database.artwork_count_all())

    def test_add_artwork_not_unique(self):
        self.add_test_data()
        artwork = Artwork(artist = 'Paul Cezanne', name='The Bathers', price = 600)
        with self.assertRaises(IntegrityError): #will not add artwork because it violates unique constraint
            artwork.save()

    def test_create_artwork_default_available_yes(self):
        artwork = Artwork(artist = 'Paul Cezanne', name='The Blue Vase', price = 600)
        artwork.save()
        self.assertTrue(artwork.is_available)
    

    def test_delete_artwork(self):
        self.add_test_data() #call helper method above to add data - 2 in artwork table
        count = database.artwork_count_all() #original count is 2
        database.delete_artwork(self.artwork2) #should be 1 after delete
        self.assertEqual(count-1, database.artwork_count_all()) #count the number of artwork pieces in the artwork table
       
    def test_delete_artwork_not_in_table_raises_error(self):
        self.add_test_data() #call helper method above to add data - 2 in artwork table
        artwork = Artwork(artist = 'Not known', name = 'Not known', price = 0)
        with self.assertRaises(ArtError):
            database.delete_artwork(artwork) 
        
    #def test_change_artwork_status(self):
     #   self.add_test_data()
      #  database.change_availability(self.artwork1)
        #self.assertFalse(self.artwork1.is_available)
       # self.assertFalse(self.artwork1.is_available)

    
    def test_artwork_count_all(self):
        self.add_test_data()
        count = database.artwork_count_all()
        self.assertEqual(2, count)

    
    
    
    

    #if __name__ == '__main__':
    #unittest.main()
       
        