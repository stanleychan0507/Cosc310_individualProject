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

    # def test_output(self):
    # do some test to see if the conversation flows
    # e.g. in reviewMessage, is positiveService revoke if review > 7? .....etc.

    # def test_negativeReview(self):
    # do some tes to see if the output is correct.
    # e.g. if answer is "yes", would it output deepservice(serviceName)?
    # if answer is "no", would it print "Thanks for your feedback"
    # if answer is either yes or no, would it print "Didn't quite get that....."

if __name__ == '__main__':
    unnitest.main()