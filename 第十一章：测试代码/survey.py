class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.resposes = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答案"""
        self.resposes.append(new_response)

    def show_result(self):
        """显示所有答案"""
        print('Survey Result:' )
        for response in self.resposes:
            print(f"- {response.title()}")
