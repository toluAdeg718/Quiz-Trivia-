class QuizBrain:

    def __init__(self, question_list):
        self.question_n = 0
        self.list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_n < len(self.list)

    def new_question(self):
        current_question = self.list[self.question_n]
        self.question_n +=1
        user_answer = input(f"Q.{self.question_n}{current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it Right")

        else:
            print("that's wrong. ")
        print(f"The correct answer was: {correct_answer}.")
        print(f" Your current score is {self.score}/{self.question_n}. ")
