from pickle import APPEND
import unittest
import assignment_part2_david_Le as ChatBot

class TestBot(unittest.TestCase):
    @Test
    def setUp(self):
        # Load test data
        self.app = APPEND(chatbot='assignment_part2_david_Le.py')

    def test_writeReview(self):
        # Test case 1 : 
        userInput = self.app.name()
        self.assertEquals("inputString", userInput.notNull().asString())

    def test_output(self):
        # Test case 2 :
        self.reviewMessage("pedicure")
        self.assertEquals(1, positiveService("pedicure"))

    def test_negativeReview(self):
        # Test case 3 :
        self.rememberReview()
        name = "Bob"
        recommend = "y"
        goodPoint = "goodPoint statement here"
        feedback = "feedback statement here"
        self.assertEquals(1, print("""Your review has been saved!
            would you recommend {name}: {recommend}
            what did we do well: {goodPoint}
            how can we do better: {feedback}"""))

if __name__ == '__main__':
    unnitest.main()