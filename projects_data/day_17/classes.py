# create a new Question class

class Question:

    def __init__(self, text, answer):
        """Initialize the Question class with a text and an answer"""

        self.text = text
        self.answer = answer

# create a new QuizBrain class

class QuizBrain:

    def __init__(self, question_list):

        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        
        answer = input(f"Q.{self.question_number + 1}. {self.question_list[self.question_number].text} (True/False)?: ").capitalize()
        self.question_number += 1
        return answer

    def still_has_questions(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer):

        question_to_check = self.question_number - 1

        if self.question_list[question_to_check].answer == answer:
            self.score += 1
            print("You are right!")
        else:
            print("Bad answer!")
        print(f"Your actual score is {self.score}/{self.question_number}.\n")



