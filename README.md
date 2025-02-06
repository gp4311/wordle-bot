# Wordle Bot
Wordle Bot is an automated solver for the popular [Wordle](https://www.nytimes.com/games/wordle/index.html) game. It leverages algorithmic strategies and linguistic analysis to guess the secret five-letter word within six attempts. This project is implemented in Python and demonstrates techniques in search algorithms, filtering logic, and information theory.

## Features

- **Automated Gameplay:** Simulates the Wordle game by selecting a random secret word and iteratively guessing based on feedback.
- **Feedback Processing:** Interprets letter feedback as:
  - **Green:** Correct letter in the correct position.
  - **Yellow:** Correct letter in the wrong position.
  - **Gray:** Letter not in the secret word.
- **Candidate Filtering:** Dynamically narrows down the list of possible words based on previous guess feedback.
- **Extensible Strategy:** Basic implementation picks the next guess from the remaining candidate pool. The framework allows for integration of more advanced strategies (e.g., frequency analysis, entropy calculation).

## Getting Started

### Prerequisites

- Python 3.7 or later
- Basic knowledge of the command line

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/wordle-bot.git
   cd wordle-bot

2. **Install any dependencies:**

    ```bash
    pip install -r requirements.txt

## Usage

To run the Wordle Bot simulation, execute the following command:

    ```bash
    python wordle_bot.py

The script will:
1. Start with a predetermined initial guess.
2. Process the feedback from each guess and filter the candidate list.
3. Continue guessing until the word is found or the maximum of 6 attempts is reached.

## Acknowledgements

Inspired by the original Wordle game by Josh Wardle
