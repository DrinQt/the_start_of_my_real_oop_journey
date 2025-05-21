import random
from question import Question

class Quiz:
    def __init__(self, file_name):
        self.file_name = file_name
        self.questions = self.load_questions()

    def load_questions(self):
        questions = []
        try:
            with open(self.file_name, 'r') as file:
                content = file.read().split('\n\n')  # Split by double newlines
                for block in content:
                    lines = block.strip().split('\n')
                    if len(lines) < 2:  # Ensure we have at least a question and an answer
                        continue

                    question_text = lines[0].strip()  # First line is the question
                    options = [line.strip() for line in lines[1:-1]]  # All lines except the last one are options
                    correct_answer_line = lines[-1]  # Last line is the correct answer

                    # Getting the correct answer
                    if "Correct Answer :" in correct_answer_line:
                        correct_answer = correct_answer_line.split(':')[-1].strip().lower()
                        questions.append(Question(question_text, options, correct_answer))
                    else:
                        print(f"Skipping Invalid block: {block}")
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return questions

    def play(self):
        if not self.questions:
            print("No questions available.")
            return

        while True:
            question = random.choice(self.questions)  # Randomly select a question
            question.ask()

            # Ask if the user wants to continue
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing my Quiz!")
                break
