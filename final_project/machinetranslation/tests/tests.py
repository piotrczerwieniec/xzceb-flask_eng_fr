import unittest

from translator.py import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french(None), None)  # test when Null is given as input the output is Null.
        


class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english(None), None) # test when Null is given as input the output is null.
     
unittest.main()