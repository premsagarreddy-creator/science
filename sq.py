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

