# -*- coding: utf-8 -*-

# Note, we make calls to WikiData API - a collective, internet-based concept store.
# Tests won't work without Internet connection. We could implement the downloads.
# Make sure you have connectivity to:
#     https://www.wikidata.org/w/api.php

import unittest
import asterisk as rx

PREFER_TEST_WITH_WIKIDATA = False

if PREFER_TEST_WITH_WIKIDATA:
    import socket
    REMOTE_SERVER = "www.wikidata.org"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 443), 2)
            return True
        except:
            pass
        return False
    WIKIDATA_CONNECTIVITY = is_connected()
else:
    WIKIDATA_CONNECTIVITY = False

class TestConcepts(unittest.TestCase):

    def test_dog_cat(self):
        ''' Test if we can use "multilingual words", in other words,
            "Concepts" to represent assets. '''

        if WIKIDATA_CONNECTIVITY:
            Dog = rx.Concept('Q144')
            Cat = rx.Concept('Q146')
        else:
            Dog = rx.Concept({'zh': u'狗'})
            Cat = rx.Concept({'de': 'Katze'})

        # We want a dog.
        dog = Dog()
        # We want a cat.
        cat = Cat()

        self.assertEqual(dog.aliases['zh'][0]['value'], u'狗')
        self.assertEqual(cat.aliases['de'][0]['value'], u'Katze')

    def test_properties(self):
        ''' Test if we can define custom properties to them as dictionaries.
            After all, we want to index the real items of the world.
        '''
        if WIKIDATA_CONNECTIVITY:
            Dog = rx.Concept('Q144')
            Cat = rx.Concept('Q146')
        else:
            Dog = rx.Concept({'zh': u'狗'})
            Cat = rx.Concept({'de': 'Katze'})

        # We want a dog with 4 legs, owned by Bob.
        dog = Dog({'legs': 4,
                   'owner': 'Bob'})

        # We want a cat with 4 legs, owned by Alice.
        cat = Cat({'legs': 4,
                   'owner': 'Alice'})

        self.assertEqual(dog.details, {'legs': 4, 'owner': 'Bob'})
        self.assertEqual(cat.details, {'legs': 4, 'owner': 'Alice'})

    def test_defining_reality(self):
        '''
            Defining a real fact.
        '''
        # Input
        if WIKIDATA_CONNECTIVITY:
            Universe = rx.Concept('Q1')
        else:
            Universe = rx.Concept({'en': 'Universe', 'de': 'Universum'})

        # We have a universe with gravitational constant equal to 6.67408e-11.
        universe = Universe({'gravitational constant': 6.67408e-11}, fact=True)

        # The relity is denoted by '.' - something that's existing,
        # dot represents the already precipitated, accrued information.
        self.assertEqual(universe.sign, '.')
        self.assertEqual(universe.fact, True)

    def test_defining_desirity(self):
        '''
            Defining a desired thing.
        '''
        # Input
        if WIKIDATA_CONNECTIVITY:
            Universe = rx.Concept('Q1')
        else:
            Universe = rx.Concept({'en': 'Universe', 'zh': u'宇宙'})

        # We want a universe with gravitational constant equal to 6.69408e-11.
        universe = Universe({'gravitational constant': 6.69408e-11})

        # The desirity is denoted by asterisk '*' - something that's desired,
        # asterisk represents the perspective lines to the future.
        self.assertEqual(universe.sign, '*')
        self.assertEqual(universe.fact, False)



if __name__ == '__main__':
    unittest.main()
