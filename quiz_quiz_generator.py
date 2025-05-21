import random
from question import Question

class Quiz:
    def __init__(self, file_name):
        self.file_name = file_name
        self.questions = self.load_questions()

    def load_questions(self):
        questions = []
        try:
            with open(self.file_name, 'r') as f:
                content = f.read().split('\n\n')
                for block in content:
                    lines = block.strip().split('\n')
                    if len(lines) < 2:
                        continue
                    question_text = lines[0].strip()
                    options = [line.strip() for line in lines[1:-1]]
                    correct_line = lines[-1]
                    if "Correct Answer :" in correct_line:
                        correct = correct_line.split(':')[-1].strip().lower()
                        questions.append(Question(question_text, options, correct))
            return questions
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def play(self):
        if not self.questions:
            print("No questions available.")
            return
        while True:
            q = random.choice(self.questions)
            q.ask()
            if input("Do you want to play again? (yes/no): ").strip().lower() != "yes":
                print("Thanks for playing!")
                break
