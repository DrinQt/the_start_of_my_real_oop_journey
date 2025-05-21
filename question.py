class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def __str__(self):
        options_str = "\n".join([f"Option {chr(97 + i).upper()}: {option}" for i, option in enumerate(self.options)])
        return f"Question: {self.question_text}\n{options_str}\nCorrect answer: {self.correct_answer.upper()}"
    



    