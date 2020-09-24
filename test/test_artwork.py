from unittest import TestCase
import os
import database_config


#change database path to test_art.sqlite
database_config.database_path = 'test_art.sqlite'

<<<<<<< HEAD
import database

=======

import database


>>>>>>> 6b9950d4a53b1d34813feb30a5a1314ab5086aeb
import controller
from models import Artist, Artwork
from database import ArtError, IntegrityError

class TestArtwork(TestCase):
    
    def setUp(self):
        # connect to dbase and delete from dbase all data in each table
        Artist.delete() #deletes everything in the table
        Artwork.delete()
        

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
        artist = Artist(name = 'Nicole Tempas', email = 'nt@gmail.com')
        artist.save()
        self.assertEqual(1, database.artist_count())
    
    def test_add_artist_not_unique(self):
        self.add_test_data()
        artist3 = Artist(name = 'Paul Cezanne', email = 'pc@gmail.com') #should violate unique constraint for name and email
        artist4 = Artist(name = 'Saul Cezanne', email = 'pc@gmail.com') #should violate unique constraint for name and email
        artist5 = Artist(name = 'Paul Cezanne', email = 'cp@gmail.com') #should violate unique constraint for name and email
        
        with self.assertRaises(IntegrityError): #should raise an error because name & email not unique
            artist3.save()
            artist4.save()
            artist5.save()

            #also test name w/ different email; correct email different name

   # def test_add_artwork(self):
    #    artwork = Artwork(name='Still Life', price = 500)
     #   artwork.save()
      #  self.assertEqual(1, database.artwork_count_all())# ???



    #def test_add_artwork_already_in_table(self): #artwork name is unique
     #   self.add_test_data() #adds 2 artworks; this includes the artwork listed below
      #  artwork3 = Artwork(name = 'The Thinker', price = 500, artist = self.artist1)
        #artwork3.save() #try to save - should not be able to add as name is same as already in table
        #self.assertEqual(2, database.artwork_count_all()) #should have only 2 artworks
       # with self.assertRaises(IntegrityError):
        #    artwork3.save()

    #def test_create_artwork_default_available_yes(self):
     #       self.add_test_data()
      #      self.assertTrue(artwork1.is_available())

    
   # def test_delete_artwork(self):
    #    self.add_test_data() #call helper method above to add data - 2 in artwork table
     #   artwork.delete(artwork1)  #now only 1 piece of art is in the artwork table
      #  self.assertEqual(1, Artwork.select().count_all()) #count the number of artwork pieces in the artwork table
       # self.assertIsNone(artwork1)  #there is no artwork1 in the artwork table

    #def test_delete_artwork_not_in_table(self):
     #   pass
    
       
        