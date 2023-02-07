class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").capitalize()
        while ans != "True" and ans != "False":
            ans = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").capitalize()            
        self.check_answer(ans, current_question.get_answer())

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if correct_ans == user_ans:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def show_final_message(self):
        print("You've complete the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")