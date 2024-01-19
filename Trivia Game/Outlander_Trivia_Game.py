import random

def outlander_trivia_game():
    print("Welcome to the Outlander Trivia Game!")

    def ask_question(question_data):
        print("\n" + question_data['question'])
        
        options = question_data['options'].copy()
        random.shuffle(options)
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            user_answer = input("Your answer (enter the number): ")

            try:
                user_answer_index = int(user_answer) - 1
                user_answer_text = options[user_answer_index]

                if user_answer_index >= 0 and user_answer_index < len(options):
                    if user_answer_text == question_data['correct_answer']:
                        print("Correct!")
                        return True
                    else:
                        print(f"Wrong! The correct answer is: {question_data['correct_answer']}")
                        return False
                else:
                    print("Invalid input. Please enter a valid number.")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def run_quiz(questions):
        score = 0

        for question_data in questions:
            if ask_question(question_data):
                score += 1

        return score

    initial_questions = [
        {
            'question': "1. Who is the author of the 'Outlander' book series?",
            'options': ['Diana Gabaldon', 'George R. R. Martin', 'J.K. Rowling', 'Stephenie Meyer'],
            'correct_answer': 'Diana Gabaldon'
        },
        {
            'question': "2. What is the name of the main character in Outlander?",
            'options': ['Claire Fraser', 'Jamie Fraser', 'Brianna Randall', 'Frank Randall'],
            'correct_answer': 'Claire Fraser'
        },
        {
            'question': "3. Where does most of the Outlander series take place?",
            'options': ['England', 'Scotland', 'France', 'Ireland'],
            'correct_answer': 'Scotland'
        },
        {
            'question': "4. What is the name of Jamie Fraser's sister?",
            'options': ['Jenny', 'Marsali', 'Geillis', 'Laoghaire'],
            'correct_answer': 'Jenny'
        },
        {
            'question': "5. Who is the actor that plays Jamie Fraser in the Outlander TV series?",
            'options': ['Sam Heughan', 'Tobias Menzies', 'Graham McTavish', 'David Berry'],
            'correct_answer': 'Sam Heughan'
        }
    ]

    harder_questions = [
        {
            'question': "6. What year does Claire Randall initially time travel to in Outlander?",
            'options': ['1743', '1776', '1968', '1865'],
            'correct_answer': '1743'
        },
        {
            'question': "7. What is the name of Jamie's godfather and best friend?",
            'options': ['Murtagh', 'Dougal', 'Angus', 'Rupert'],
            'correct_answer': 'Murtagh'
        },
        {
            'question': "8. What is the name of the standing stones through which Claire time travels?",
            'options': ['Craigh na Dun', 'Stonehenge', 'Avebury', 'Callanish'],
            'correct_answer': 'Craigh na Dun'
        },
        {
            'question': "9. What profession does Claire have in the 20th century?",
            'options': ['Nurse', 'Doctor', 'Teacher', 'Engineer'],
            'correct_answer': 'Nurse'
        },
        {
            'question': "10. What is the name of Jamie and Claire's daughter?",
            'options': ['Brianna', 'Fiona', 'Marsali', 'Laoghaire'],
            'correct_answer': 'Brianna'
        }
    ]
    
    extra_hard_questions = [
        {
            'question': "11. In which Scottish clan is Jamie a member?",
            'options': ['MacKenzie', 'MacDonald', 'Fraser', 'Cameron'],
            'correct_answer': 'Fraser'
        },
        {
            'question': "12. What is the title of the first book in the Outlander series?",
            'options': ['Outlander', 'Dragonfly in Amber', 'Voyager', 'Drums of Autumn'],
            'correct_answer': 'Outlander'
        },
        {
            'question': "13. What is the name of Jamie's nephew who becomes a key character in later books?",
            'options': ['Roger', 'Ian', 'Fergus', 'William'],
            'correct_answer': 'Ian'
        },
        {
            'question': "14. What historical event is a major backdrop in the Outlander series?",
            'options': ['Jacobite Rising / Battle of Culloden', 'World War II', 'French Revolution', 'Civil War'],
            'correct_answer': 'Jacobite Rising / Battle of Culloden'
        },
        {
            'question': "15. What is the name of Jamie's printshop in Edinburgh?",
            'options': ['A. Malcolm & Co.', 'Fraser & Sons', 'Heughan & MacTavish', 'Highland Printers'],
            'correct_answer': 'A. Malcolm & Co.'
        }
    ]
    
    extra_extra_hard_questions = [
        {
            'question': "16. What is the nickname given to Jamie Fraser by the Mohawk tribe?",
            'options': ['Red Jamie', 'White Wolf', 'Sassenach', 'Hawk-eye'],
            'correct_answer': 'Red Jamie'
        },
        {
            'question': "17. What is the name of the ship that brings Jamie and Claire to the American colonies?",
            'options': ['Endeavour', 'Artemis', 'Porpoise', 'Gloriana'],
            'correct_answer': 'Artemis'
        },
        {
            'question': "18. Which historical figure does Claire meet during her time in 18th-century France?",
            'options': ['Louis XIV', 'Marie Antoinette', 'Napoleon Bonaparte', 'Catherine de Medici'],
            'correct_answer': 'Louis XIV'
        },
        {
            'question': "19. What is the name of Jamie's illegitimate son?",
            'options': ['Roger MacKenzie', 'William Ransom', 'Fergus Fraser', 'Ian Murray'],
            'correct_answer': 'William Ransom'
        },
        {
            'question': "20. In the book series, what is the name of the mysterious ghost who appears in various scenes?",
            'options': ['Frank Randall', 'Jonathan Randall', 'Geillis Duncan', 'Master Raymond'],
            'correct_answer': 'Master Raymond'
        }
    ]

    initial_score = run_quiz(initial_questions)

    print("\nYou scored", initial_score, "out of", len(initial_questions), "in the initial round.")

    if initial_score == len(initial_questions):
        proceed_to_harder = input("Congratulations! You've unlocked the harder round. Do you want to proceed? (yes/no): ")

        if proceed_to_harder.lower() == 'yes':
            harder_score = run_quiz(harder_questions)

            print("\nYour score is:", initial_score + harder_score)

            if harder_score == len(harder_questions):
                proceed_to_extra_hard = input("Great job! You've unlocked the extra hard round. Do you want to proceed? (yes/no): ")

                if proceed_to_extra_hard.lower() == 'yes':
                    extra_hard_score = run_quiz(extra_hard_questions)

                    print("\nYour score is:", initial_score + harder_score + extra_hard_score)

                    if extra_hard_score == len(extra_hard_questions):
                        proceed_to_extra_extra_hard = input("Outstanding! You've unlocked the extra extra hard round. Do you want to proceed? (yes/no): ")

                        if proceed_to_extra_extra_hard.lower() == 'yes':
                            extra_extra_hard_score = run_quiz(extra_extra_hard_questions)

                            print("\nYour final score is:", initial_score + harder_score + extra_hard_score + extra_extra_hard_score)

                            if extra_extra_hard_score == len(extra_extra_hard_questions):
                                print("Incredible! You got all the questions right. You're a true Outlander expert!")
                            else:
                                print("Good effort! You completed the extra extra hard round.")
                        else:
                            print("Thanks for playing! You completed the extra hard round.")
                    else:
                        print("Thanks for playing! You completed the harder round.")
                else:
                    print("Thanks for playing! You completed the initial round.")
            else:
                print("Thanks for playing! You did not unlock the extra hard round.")
        else:
            print("Thanks for playing! You completed the initial round.")
    else:
        print("Thanks for playing! You did not unlock the harder round.")

outlander_trivia_game()