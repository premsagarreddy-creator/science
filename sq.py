def science_quiz():
    """Main function placeholder for Science Quiz."""
    pass
def print_banner():
    print("Welcome to the Science Quiz!")
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
def print_banner():
    print(CYAN + "\n📘 Welcome to the Science Quiz! 📘\n" + RESET)
def print_question(q, options):
    print(YELLOW + q + RESET)
    for key, val in options.items():
        print(f"  {key}) {val}")
def get_valid_input():
    while True:
        ans = input("Enter your answer (a/b/c/d): ").lower()
        if ans in ['a', 'b', 'c', 'd']:
            return ans
        print(RED + "Invalid input, try again." + RESET)
def ask_question(question, options, correct):
    print_question(question, options)
    answer = get_valid_input()
    if answer == correct:
        print(GREEN + "Correct!\n" + RESET)
        return True
    else:
        print(RED + f"Wrong! Correct answer is '{correct}'.\n" + RESET)
        return False
def question1():
    return ask_question(
        "What is H2O commonly known as?",
        {'a': 'Hydrogen Peroxide', 'b': 'Salt', 'c': 'Water', 'd': 'Oxygen'},
        'c'
    )
def question2():
    return ask_question(
        "Which part of the plant conducts photosynthesis?",
        {'a': 'Root', 'b': 'Stem', 'c': 'Leaf', 'd': 'Flower'},
        'c'
    )
def question3():
    return ask_question(
        "Which planet is known as the Red Planet?",
        {'a': 'Earth', 'b': 'Mars', 'c': 'Jupiter', 'd': 'Venus'},
        'b'
    )

