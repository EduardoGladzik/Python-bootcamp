from data import feedback_data
class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Questão {self.question_number} / {current_question.category} / {current_question.difficulty}")
        print(f"{current_question.text}")
        user_answer = input(f"Digite sua resposta: ")
        self.check_answer(user_answer, current_question.answer, current_question.difficulty)
    
    def check_answer(self, user_answer, correct_answer, quesition_difficulty):
        if user_answer.lower() == correct_answer.lower():
            if quesition_difficulty == "difícil":
                self.score += 3
            elif quesition_difficulty == "médio":
                self.score += 2
            else:
                self.score += 1
            print(feedback_data["correct"])
        else:
            print(feedback_data["incorrect"])
            print(f"A resposta correta era: {correct_answer}")
        print(f"Pontuação atual: {self.score} pontos\n")