from quiz import Quiz

def main():
    quiz = Quiz("quiz_questionnaires.txt")
    quiz.add_questions()
    quiz.save()

if __name__ == "__main__":
    main()
