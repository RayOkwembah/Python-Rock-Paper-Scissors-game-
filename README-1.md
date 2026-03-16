# 🎮 Rock Paper Scissors

A command-line Rock Paper Scissors game built in Python with a win/loss tracker.

## Features

- Play against the computer
- Tracks wins, losses, and ties across rounds
- Input validation with helpful error messages
- Clean score display after each round

## How to Run

Make sure you have Python 3 installed, then:

```bash
python rock_paper_scissors.py
```

## How to Play

1. Type `rock`, `paper`, or `scissors` and press Enter
2. The computer randomly picks its choice
3. The result and updated score are shown after each round
4. Type `quit` to exit and see your final score

## Example

```
===================================
      🎮 Rock Paper Scissors!
===================================
Type 'quit' to exit

Your choice (rock/paper/scissors): rock

You chose:      rock
Computer chose: scissors
✅ You win!
Score → Wins: 1 | Losses: 0 | Ties: 0 | Total: 1
```

## Concepts Used

- Functions and docstrings
- Dictionaries for game logic
- Loops and input validation
- `if __name__ == "__main__"` pattern

## Possible Extensions

- [ ] Save scores to a JSON file between sessions
- [ ] Add a best-of-5 mode
- [ ] Add Lizard and Spock variants
- [ ] Track win streaks
