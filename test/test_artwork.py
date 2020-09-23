from unittest import TestCase
import os

#import database_config
#database_config.database_path = 'database/test_art.sqlite'

import controller
from models import Artist, Artwork, ArtError

class TestArtwork(TestCase):
    @classmethod
    def setUpClass(cls):   
        #name used in testing =#swap real db, with test db
        #artstore.db =os.path.join('art.sqlite', 'test_art.sqlite')
        
       # controller.db = os.path.join('database', 'test_art.slite')
        Artstore.instance=None#?clearing out previously used test dbase
        

    def setUp(self):
        self.AS = Artstore() #create new instance of test-dbase?
        self.clear_artstore()  #and clear it


    def add_test_data(self): #helper/utility method
        self.clear_artstore()  #clear the test dbase

        #which of these 2 do I do?
        self.artist1=Artist('Auguste Rodin', 'ar@gmail.com')
        self.artist1 = Artist(name = 'Auguste Rodin', email = 'ar@gmail.com')
        
        self.artist2 = Artist('Paul Cezanne', 'pc@gmail.com')
        self.artist1.save()
        self.artist2.save()
        
        self.artwork1 = Artwork('The Thinker', 500, artist1)
        self.artwork1.save()
        self.artwork2 = Artwork('The Bathers', 600, artist2)
        self.artwork2.save()

    def clear_artstore(self): #another helpermethod
        self.AS.delete_all_artists()
        self.AS.delete_all_artwork()


    def test_add_artist(self):
        artist = Artist('Nicole Tempas', 'nt@gmail.com')
        artist.save()
        self.assertEqual(1, self.AS.artist_count())
        
#?????/would this be 3 because setup already added 2 artists?
        #test adding duplicate raises error?
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