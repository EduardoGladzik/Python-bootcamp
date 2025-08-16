import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)  # Convert Ace from 11 to 1
        score = sum(hand)
    return score

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

    while input("Type 'y' to get another card, type 'n' to pass:") != 'n':
        player_hand.append(deal_card())
        if calculate_score(player_hand) > 21:
            print(f"Your final hand: {player_hand}, final score: {calculate_score(player_hand)}")
            print("You went over. You lose")
            return
        print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
    else:
        while calculate_score(computer_hand) < 17:
            computer_hand.append(deal_card())
        print(f"Computer's final hand: {computer_hand}, final score: {calculate_score(computer_hand)}")
        print(f"Your final hand: {player_hand}, final score: {calculate_score(player_hand)}")
    
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" + "-"*50)
    play_game()