from unittest import TestCase
import os
import database_config
import database

#change database path to test_art.sqlite
database_config.database_path = 'test_art.sqlite'

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
        self.artwork2 = Artwork(nbame = 'The Bathers', price =600, artist = self.artist2)
        self.artwork2.save()

    

    def test_add_artist(self):
        artist = Artist(name = 'Nicole Tempas', email = 'nt@gmail.com')
        artist.save()
        self.assertEqual(1, Artist.select().count())
        

"""
    def test_create_artwork_default_available_yes(self):
        artist = Artist('Auguste Rodin', 'ar@gmail.com')
        #database.add_artist(artist)
        clear_artstore.add_artist('August Rodin', 'ar@gmail.com')
        artwork = Artwork('The Thinker', 500, artist)
        controller.add_artwork(Artwork)
        #database.add_artwork(name = 'The Thinker', price = 500, artist = artist)
        self.assertTrue(artwork.is_available)
"""
"""
    def test_save_artwork_to_db(self):
        artist = Artist('August Rodin', 'ar@gmail.com')
        artstore.add_artist(artist)
        artwork= Artwork('The Thinker', 500, artist )
        artstore.add_artwork(artwork)
        
        self.assertEqual() 
        """
"""
    def test_save_change_availability_to_db(self):
        artist = Artist('Auguste Rodin', 'ar@gmail.com')
        artstore.add_artist(artist)
        artwork = Artwork('Name', 500, artist)
        artstore.add_artwork(artwork)
        """