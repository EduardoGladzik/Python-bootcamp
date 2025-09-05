# Blackjack Game

A simple Python implementation of the classic Blackjack card game.

## How to Play

- The goal is to get as close to 21 as possible without going over
- Face cards (J, Q, K) are worth 10 points
- Aces can be worth 1 or 11 points
- You can hit (get another card) or stand (keep your current hand)
- The dealer must hit until they reach 17 or higher

## Files

- `main.py` - Main game logic and gameplay
- `art.py` - ASCII art logo for the game

## Running the Game

```bash
python main.py
```

## Game Rules

- Blackjack (21 with 2 cards) beats all other hands
- If you go over 21, you lose
- If the dealer goes over 21, you win
- If neither goes over 21, the higher score wins
- Ties result in a draw
