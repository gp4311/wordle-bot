# Wordle Bot
Wordle Bot is an automated solver for the popular [Wordle](https://www.nytimes.com/games/wordle/index.html) game. It leverages algorithmic strategies and linguistic analysis to guess the secret five-letter word within six attempts. This project is implemented in Python and demonstrates techniques in search algorithms, filtering logic, and information theory.

## Features

- **Feedback Processing:**
  - Analyzes user-provided feedback for each guess and refines the possible words.
  - Implements three types of letter feedback:
    - **Green:** Correct letter in the correct position.
    - **Yellow:** Correct letter in the wrong position.
    - **Gray:** Letter not in the secret word.
- **Candidate Filtering:** Dynamically narrows down the list of possible words based on previous guess feedback.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Basic knowledge of the command line

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gp4311/wordle-bot.git
   cd wordle-bot

2. **Run the Wordle Bot:**

   ```bash
   python wordle_bot.py

## Acknowledgements

Inspired by the original Wordle game by Josh Wardle
