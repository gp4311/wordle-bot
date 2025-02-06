class Solver:
    def __init__(self, word_list):
        self.possible_words = word_list # All potential guesses the bot can make

    def process_feedback(self, guess, feedback):
        valid_words = []

        green_positions = {}
        yellow_positions = {}
        gray_letters = set()

        for i in range(5):
            letter = guess[i]

            if feedback[i] == "G": # Green feedback (correct letter, correct position)
                green_positions[i] = letter

            elif feedback[i] == "Y": # Yellow feedback (correct letter, wrong position)
                if letter in yellow_positions: 
                    yellow_positions[letter].append(i) # Allow duplicates of the same letter
                else:
                    yellow_positions[letter] = [i] # Add letter with its positions as a list
            
            elif feedback[i] == "X": # Gray feedback (letter not in the word)
                gray_letters.add(guess[i])
        
        # Filter valid words based on the feedback
        for word in self.possible_words:
            if self.is_valid_word(word, green_positions, yellow_positions, gray_letters):
                valid_words.append(word)
        
        # Update the possible words list with valid words
        self.possible_words = valid_words

    def is_valid_word(self, word, green_positions, yellow_positions, gray_letters):
        # Check Green positions (letters that must appear at the exact positions)
        for i in green_positions:
            if word[i] != green_positions[i]:
                return False

        # Check Yellow letters (letters that must appear in the word, but not in the guessed position)
        for letter in yellow_positions:
            if letter not in word:
                return False
            for pos in yellow_positions[letter]:
                if word[pos] == letter:
                    return False

        # Check Gray letters (letters that should not be in the word unless previously marked Green/Yellow)
        for letter in gray_letters:
            if letter in word and letter not in green_positions.values() and letter not in yellow_positions:
                return False

        return True

    def get_best_guess(self):
        return self.possible_words[0]