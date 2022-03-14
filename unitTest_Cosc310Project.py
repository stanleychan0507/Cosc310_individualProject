import unittest

class TestBot(unittest.TestCase):

    def setUp(self):
        # Load test data
        self.app = App(database='assignment_part2_david_Le.py')

    def test_writeReview(self):
        # test that the data type in write reviews were valid
        # e.g. 
        # type(name)=str, 
        # True if rating == 'y' else True if rating == 'n' else False, 
        # True if recommending == 'y' else True if recommending == 'n' else False, , 
        # type(purchaseDate)=str;
        userInput = type(self.app.name())
        self.assertEqual(userInput, 'str')

if __name__ == '__main__':
    unnitest.main()