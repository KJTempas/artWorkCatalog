import unittest
from unittest import TestCase
from unittest.mock import patch
from peewee import *

import db_config
db_path = 'test-art.db'
db_config.database_path = db_path

from models import Artist
import controller
import database
from database import ArtError



class ArtControllerTest(TestCase):

    def setUp(self):
        #connect to test dbase, drop and create tables
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Artist])
        self.db.create_tables([Artist])
#setup - mock data from ui
    @patch('ui.get_string', return_value='Molly Brown')
    @patch('ui.get_string', return_value='mbrown@gmail.com')
    def test_add_artist(self, mock_get_string, mock_get_string):
        controller.add_artist()#call method to add artist
        artist=Artist.get_or_none(Artist.name=='Molly Brown' and Artist.email == 'mbrown@gmail.com')
        self.assertIsNotNone(artist)

@patch('ui.get_string', return_value='Molly Brown')
    @patch('ui.get_string', return_value='mbrown@gmail.com')
    def test_add_artist_duplicate(self, mock_get_string, mock_get_string):
        Artist(name='Molly Brown', email = 'mbrown@gmail.com').save()
        controller.add_artist()#try to add artist again
        artist_count = Artist.select().count() #count # of artists in mock dbase
        self.assertEqual(1, artist_count)  #should be only one - so duplicate not added




class ArtDatabaseTest(TestCase)

    def setUp(self):
    #connect to test dbase, drop and create tables
    self.db = SqliteDatabase(db_path)
    self.db.drop_tables([Artist])
    self.db.create_tables([Artist])

    def test_add_artist(self)
        database.add_artist('Molly Brown', 'mbrown@gmail.com')
        molly_b = Artist.get_or_none(Artist.name=='Molly Brown' and Artist.email == 'mbrown@gmail.com')
        self.assertIsNotNone(molly_b) #assert that molly is in the database artist table

    def test_add_artist_duplicate(self):
        Artist(name='Molly Brown', email = 'mbrown@gmail.com'.save()
        with self.assertRaises(ArtError): #trying to add molly again should raise an derror
            database.add_artist('Molly Brown', 'mbrown@gmail.com')