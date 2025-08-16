from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from random import sample

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    question_difficulty = question["difficulty"]
    new_question = Question(question_text, question_answer, question_category, question_difficulty)
    question_bank.append(new_question)

selected_questions = sample(question_bank, 20)
quiz = QuizBrain(selected_questions)

while quiz.still_has_questions():
    quiz.next_question()

print("Parabéns, você completou o quiz!")
print(f"Pontuação final: {quiz.score} pontos")