import random
import art

player_status = {'win', 'lose'}

def display_logo():
    print(art.colored_logo)


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def display_cards(user_cards, computer_cards, is_game_over, winner=None):
    if not is_game_over:
        print(f"user_cards: {user_cards}")
        print(f"computer_cards: {computer_cards[:-1] + ['?']}")
    else:
        print(f"user_cards: {user_cards}")
        print(f"computer_cards: {computer_cards}")

def calculate_score(list_cards):
    score = sum(list_cards)
    ace_count = list_cards.count(11)
    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1
    return score

def is_black_jack(list_cards):
    score = calculate_score(list_cards)
    if len(list_cards) == 2 and score == 21: # this is black-jack
        return True
    return False

def check_win(user_cards, computer_cards, is_game_over=False):
    user_score = calculate_score(user_cards)
    is_user_blackjack = is_black_jack(user_cards)
    computer_score = calculate_score(computer_cards)
    is_computer_blackjack = is_black_jack(computer_cards)

    winner = ''
    if user_score > 21:
        winner = 'computer'
        is_game_over = True
    elif computer_score > 21:
        winner = 'user'
        is_game_over = True
    elif is_user_blackjack and not is_computer_blackjack:
        winner = 'user'
        is_game_over = True
    elif is_computer_blackjack and not is_user_blackjack:
        winner = 'computer'
        is_game_over = True
    elif is_user_blackjack and is_computer_blackjack:
        winner = 'draw'
        is_game_over = True
    elif is_game_over:
        if computer_score < user_score <= 21:
            winner = 'user'
        elif user_score < computer_score <= 21:
            winner = 'computer'
        elif user_score == computer_score:
            winner = 'draw'

    return winner, is_game_over, user_score, computer_score



def hit_or_stand(user_cards, computer_cards):
    print('#' * 20)
    result = input("do you want to draw another card? hit(h) or stand(s): ")
    while result not in ("h", "s"):
        result = input("Please enter 'h' for hit or 's' for stand: ")
    if result == "h":
        user_cards.append(deal_card())
    if result == "s":
        computer_score = calculate_score(computer_cards)
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print('#' * 20)
    return result



def display_game_result(winner, user_score, computer_score):
    print('*' * 40)
    print(f"winner: {winner}")
    print(f"user_score: {user_score}")
    print(f"computer_score: {computer_score}")



def start_game():
    display_logo()
    is_game_over = False

    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    display_cards(user_cards, computer_cards, is_game_over)

    # Initial check for Blackjacks
    if is_black_jack(user_cards) or is_black_jack(computer_cards):
        winner, is_game_over, user_score, computer_score = check_win(user_cards, computer_cards, is_game_over=True)
        display_cards(user_cards, computer_cards, is_game_over, winner)
        display_game_result(winner, user_score, computer_score)
        return

    while not is_game_over:
        action = hit_or_stand(user_cards, computer_cards)
        if action == "s":
            is_game_over = True

        winner, is_game_over, user_score, computer_score = check_win(user_cards, computer_cards, is_game_over)
        display_cards(user_cards, computer_cards, is_game_over, winner)

        if is_game_over:
            display_game_result(winner, user_score, computer_score)
            break





def main():
   start_game()


if __name__ == "__main__":
    main()
