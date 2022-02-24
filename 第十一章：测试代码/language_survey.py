from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

print("显示问题并存储答案啊")
my_survey.show_question()
print("Enter 'q' at any time to quit.")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("查看文件答案")
my_survey.show_result()