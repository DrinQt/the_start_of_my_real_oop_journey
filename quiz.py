from question import Question

class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def add_questions(self):
        while True:
            q_text = input("Enter your question: ")
            opts = []
            for opt in ["A", "B", "C", "D"]:
                opts.append(input(f"Enter option {opt}: "))
            correct = input("Enter the correct answer (A, B, C, or D): ").upper()
            while correct not in ["A", "B", "C", "D"]:
                print("Invalid input. Please enter A, B, C, or D.")
                correct = input("Enter the correct answer (A, B, C, or D): ").upper()

            self.questions.append(Question(q_text, opts, correct))

            if input("Add another question? (yes/no): ").lower() != "yes":
                break

    def save(self):
        with open(self.filename, "w") as file:
            for q in self.questions:
                file.write(str(q) + "\n")
