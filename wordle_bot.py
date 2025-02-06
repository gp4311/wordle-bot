from solver import Solver

def load_word_list(filename="valid_guesses.txt"):
    # Loads the word list from the file
    # Returns a list of words that can be used in the bot
    try:
        with open(filename, "r") as file:
            words = [line.strip().lower() for line in file if line.strip()]
        if not words:
            raise ValueError("Error: The word list is empty.")
        return words
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        exit(1)

def main():
    word_list = load_word_list()
    solver = Solver(word_list)

    print("Welcome to Wordle Bot!")

    while True:
        guess = input("Enter a guess (or type 'exit' to quit): ").strip().lower()
        if guess == "exit":
            break
        if guess not in word_list:
            print("Invalid word. Please enter a valid guess from the word list.")
            continue
        
        feedback = input("Enter feedback (G for 🟩, Y for 🟨, X for ⬜): ").strip().upper()
        if len(feedback) != 5 or any(c not in "GYX" for c in feedback):
            print("Invalid feedback. Please enter exactly 5 characters (G, Y, X).")
            continue

        solver.process_feedback(guess, feedback)
        next_guess = solver.get_best_guess()
        print(f"Next suggested guess: {next_guess}")

if __name__ == "__main__":
    main()