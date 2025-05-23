
Science Quiz Module
Includes a multiple-choice science quiz game with scoring and replay.
"""

import time #used for timer in the quiz

# Color constants for styling
# Adding colors for styling
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
PURPLE = '\033[96m'
RESET = '\033[0m'

def print_banner(): #Displays the welcome banner for the quiz with styled color and emoji.
    print(CYAN + "\n📘 Welcome to the Science Quiz! 📘\n" + RESET)

def print_question(q, options): #Prints a multiple-choice question and its options in a formatted, colored style.
    print(YELLOW + q + RESET)
    for key, val in options.items():
        print(f"  {key}) {val}")

def safe_input(prompt): #A safer version of input
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting.")
        exit()

def get_valid_input():
    while True:
        ans = safe_input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)

def ask_question(question, options, correct):
    """
Ask a multiple-choice question, check the user's answer, and return whether it's correct.
"""

    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False

def question_number_1():
    return ask_question(
        "Which gas is most abundant in the Earth's atmosphere?",
        {'a': 'Oxygen', 'b': 'Carbon Dioxide', 'c': 'Nitrogen', 'd': 'Hydrogen'},
        'c'
    )


def question2():
    return ask_question(
        "Which part of the plant conducts photosynthesis?",
        {'a': 'Root', 'b': 'Stem', 'c': 'Leaf', 'd': 'Flower'},
        'c'
    )

definition question3():
    return ask_question(
        "Which planet is known as the Red Planet?",
        {'a': 'Earth', 'b': 'Mars', 'c': 'Jupiter', 'd': 'Venus'},
        'b'
    )

def question4():
    return ask_question(
        "What gas do humans need to breathe?",
        {'a': 'Nitrogen', 'b': 'Hydrogen', 'c': 'Oxygen', 'd': 'Carbon Dioxide'},
        'c'
    )

def question5():
    return ask_question(
        "What force pulls objects toward the Earth?",
        {'a': 'Magnetism', 'b': 'Friction', 'c': 'Electricity', 'd': 'Gravity'},
        'd'
    )

questions = [question1, question2, question3, question4, question5]

def loading():
    print("Loading questions", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def show_score(score, total):
    print(f"\nYou scored {score}/{total}!")
    if score == total:
        print("🏆 Excellent! Perfect score!")
    elif score >= total * 0.6:
        print("👍 Good job!")
    else:
        print("📘 Keep learning!")

def ask_replay():
    answer = safe_input("Do you want to play again? (y/n): ").lower()
    if answer == 'y':
        run_science_quiz()
    else:
        print("Thanks for playing!")

def run_science_quiz():
    """Execute the complete science quiz, including questions, score calculation, and replay option."""
    print_banner()
    loading()
    score = 0
    for q in questions:
        if q():
            score += 1
    show_score(score, len(questions))
    ask_replay()

if __name__ == "__main__":
    run_science_quiz()

