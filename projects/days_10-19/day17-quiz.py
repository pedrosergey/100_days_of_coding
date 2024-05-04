# import the questions

from project_data.day_17.question_bank import question_data
from project_data.day_17.classes import QuizBrain, Question
from project_data.ascii_images import day17_logo
import random as r


# create a bank of questions objects using the Question class

list_of_questions_objects = []

for question in question_data:

    question_to_add = Question(question["text"], question["answer"])
    list_of_questions_objects.append(question_to_add)


# # start the game

print(day17_logo)
print("Welcome to the MAGIC QUIZZ!\n")

first = QuizBrain(list_of_questions_objects)

while first.still_has_questions():

    first.check_answer(first.next_question())

print("You have successfully complete the quiz!")
print(f"Your final score was: {first.score}/{first.question_number}.")