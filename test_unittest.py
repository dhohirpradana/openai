import unittest
from my_sum import sum
from openai_question import getAnswer


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        assert 1 + 1 == 2, "Should be 2"

    def test_decrement(self):
        assert 2 - 1 == 1, "Should be 1"

    def test_sum(self):
        data=[1, 2, 3]
        result=sum(data)
        
        self.assertEqual(result, 6, "Should be 6")
        # self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        
    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6, "Should be 6")
    
    # http request test
    def test_getAnswer(self):
        question = "What is the capital of America?"
        answer = getAnswer(question)
        print('answer:', answer)


if __name__ == '__main__':
    unittest.main()
