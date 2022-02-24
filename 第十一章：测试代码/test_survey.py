import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善处理"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.resposes)

    def test_store_three_responses(self):
        """测试3个答案"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        # my_survey.store_response(['english', 'chinese', 'spanish'])
        responses = ['english', 'chinese', 'spanish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.resposes)


if __name__ == '_main_':
    unittest.main()
