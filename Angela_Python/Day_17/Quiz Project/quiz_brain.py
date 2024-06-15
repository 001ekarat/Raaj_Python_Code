'''
Create a class QuizBrain. write an __init__() method.
initialise the question_number to 0.
initialise the question_list to an input.
'''

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You gpot it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was :{correct_answer}.")
        print(f"your current score is : {self.score}/{self.question_number}")
        print("\n")


'''
Retrive the item at the current question_number fro the question_list.
Use the input() function to show the user the question text and ask for the user's answer.
'''


