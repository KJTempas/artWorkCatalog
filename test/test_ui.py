from unittest import TestCase
from unittest.mock import patch

import ui


class TestUI(TestCase):

    #patch is a library that allows mock testing; side_effect is the answer expected
    #testing to see if what I want to return is returned
    @patch('builtins.input', side_effect =['apples'])
    def test_get_string(self,  mock_input):
        self.assertEqual('apples', ui.get_string('What is your favorite fruit?'))
        