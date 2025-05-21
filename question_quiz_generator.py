class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def ask(self):
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{chr(97 + i)}. {option}")
        user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        if user_answer == self.correct_answer:
            print("Galing ah! You got it right!")
        else:
            print(f"Mali! Wrong answer! The correct answer is: {self.correct_answer}")
