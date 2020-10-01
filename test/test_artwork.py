#import unittest
from unittest import TestCase
import database_config

#change database path to test_art.sqlite
database_config.database_path = 'test_art.sqlite'
import database

import controller
from models import Artist, Artwork
from database import ArtError, IntegrityError

class TestArtwork(TestCase):
    
    def setUp(self): # runs before every test 
        # connect to dbase and delete from dbase all data in each table
        Artist.delete().execute() #deletes everything in the table
        Artwork.delete().execute()
        

    def add_test_data(self): #helper/utility method
        self.artist1 = Artist(name = 'Auguste Rodin', email = 'ar@gmail.com')
        self.artist2 = Artist(name = 'Paul Cezanne', email = 'pc@gmail.com')
        self.artist1.save()
        self.artist2.save()
        
        self.artwork1 = Artwork(name_of_artwork = 'The Thinker', price = 500, artist = self.artist1)
        self.artwork1.save()
        self.artwork2 = Artwork(name_of_artwork = 'The Bathers', price =600, artist = self.artist2)
        self.artwork2.save()


    def test_add_artist(self):
        artist = Artist(name = 'Quinn Tempas', email = 'qt@gmail.com')
        artist.save()
        self.assertEqual(1, database.artist_count())
    
   # def test_add_artist_using_database_file_method(self):
    #    name = 'Quinn Tempas'
     #   email = 'qt@gmail.com'
      #  database. add_artist(name,email)
       # self.assertEqual(1, database.artist_count)

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
           
   # def test_add_artist_no_name(self):
    #    artist6 = Artist(name = 'Not known', email = 'test@gmail.com')
     #   with self.assertRaises(ArtError):
      #      artist6.save()

    def test_add_artwork(self):
        self.add_test_data() #to make sure artist is in the artist table
        artwork = Artwork(artist = 'Paul Cezanne', name_of_artwork='The Blue Vase', price = 600)
        artwork.save()
        self.assertEqual(3, database.artwork_count_all())

    def test_add_artwork_not_unique(self):
        self.add_test_data()
        artwork = Artwork(artist = 'Paul Cezanne', name_of_artwork='The Bathers', price = 600)
        with self.assertRaises(IntegrityError): #will not add artwork because it violates unique constraint
            artwork.save()

    def test_create_artwork_default_available_yes(self):
        artwork = Artwork(artist = 'Paul Cezanne', name_of_artwork='The Blue Vase', price = 600)
        artwork.save()
        self.assertTrue(artwork.is_available)
    

    def test_delete_artwork(self):
        self.add_test_data() #call helper method above to add data - 2 in artwork table
        database.delete_artwork('The Bathers') #should be 1 after delete
        self.assertEqual(1, database.artwork_count_all()) #count the number of artwork pieces in the artwork table
       
    #def test_delete_artwork_not_in_table_raises_error(self):
     #   self.add_test_data() #call helper method above to add data - 2 in artwork table
        ##artwork = Artwork(artist = 'Not known', name = 'Not known', price = 0)
      #  with self.assertRaises(ArtError):
       #     database.delete_artwork('Testing123') 
        
    def test_change_artwork_status(self):
        self.add_test_data()
        self.artwork1.is_available = False
        #database.change_availability(self.artwork1.is_available == False)
        self.assertFalse(self.artwork1.is_available)
       
    def test_show_all_artists(self):
        self.add_test_data() #test data has 2 artists
        count = database.artist_count()
        self.assertEqual(2, count)

    def test_show_all_artist_when_no_artists(self):
        count = database.artist_count()
        self.assertEqual(0,count)
    
    def test_show_artwork_by_one_artist(self):
        self.add_test_data()
        artwork_by_artist = database.show_artwork_by_one_artist(self.artist2)
        list(artwork_by_artist)
        self.assertEqual(1, len(artwork_by_artist)) # so len of artworks should be 2

    def test_show_artwork_by_one_artist_not_in_dbase(self):
        self.add_test_data()
        artworks = database.show_artwork_by_one_artist('Not known') #artworks should be an empty list
        list(artworks) #make a list so can see length
        self.assertEqual(0, len(artworks))

    def test_artwork_count_all(self):
        self.add_test_data()
        count = database.artwork_count_all()
        self.assertEqual(2, count)

    def test_artist_count(self):
        self.add_test_data()
        count = database.artist_count()
        self.assertEqual(2, count)
    
    def test_get_artist_by_name(self):
        self.add_test_data()
        self.assertEqual('pc@gmail.com', database.find_artist('Paul Cezanne').email)

    def test_get_artist_by_name_not_in_dbase(self):
        self.assertIsNone(database.find_artist('Fred Chopin'))

    
    
    

    #if __name__ == '__main__':
     #   unittest.main()
       
        