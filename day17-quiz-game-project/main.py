from question_model import Question
import data
from quiz_brain import QuizBrain

question_bank = []
for q in data.question_data:
    question_bank.append(Question(q["text"], q["answer"]))

q= QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()
q.show_final_message()