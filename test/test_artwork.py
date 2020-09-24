from unittest import TestCase
import os
import database_config


#change database path to test_art.sqlite
database_config.database_path = 'test_art.sqlite'


import database


import controller
from models import Artist, Artwork
from database import ArtError

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

#????when do I need to use self.

    def test_add_artist(self):
        artist = Artist(name = 'Nicole Tempas', email = 'nt@gmail.com')
        artist.save()
        #self.assertEqual(1, Artist.select().count())  #doesn't like Artist
        #self.assertEqual(1, self.database.artist_count()) #doesn't like self
        self.assertEqual(1, database.artist_count())

    def test_add_artwork(self):
        artwork = Artwork(name='Still Life', price = 500)
        artwork.save()
        self.assertEqual(1, database.artwork_count_all())# ???

    def test_create_artwork_default_available_yes(self):
        self.add_test_data()
        self.assertTrue(artwork1.is_available())
    
    def test_create_artwork_already_in_table(self): #artwork name is unique
        self.add_test_data() #adds 2 artworks; this includes the artwork listed below
        self.artwork3 = Artwork(name = 'The Thinker', price = 500, artist = self.artist1)
        self.artwork3.save() #try to save - should not be able to add as name is same as already in table
        self.assertEqual(2, database.artwork.count_all()) #should have only 2 artworks


    
    def test_delete_artwork(self):
        self.add_test_data() #call helper method above to add data - 2 in artwork table
        artwork.delete(artwork1)  #now only 1 piece of art is in the artwork table
        self.assertEqual(1, Artwork.select().count_all()) #count the number of artwork pieces in the artwork table
        self.assertIsNone(artwork1)  #there is no artwork1 in the artwork table

    def test_delete_artwork_not_in_table(self):
        pass
    
       
        