import art2
import random
import os


def deal() -> int:
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


player = []
dealer = []

while True:
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    if play_game == 'n':
        break
    else:
        os.system("clear")  # Linux - OSX
        os.system("cls")  # Windows - OSX
        print(art2.logo)

        # deal both user and dealers starting hand
        for _ in range(2):
            player.append(deal())
            if 11 in player and sum(player) > 21:
                location = player.index(11)
                player[location] = 1

            dealer.append(deal())
            if 11 in dealer and sum(dealer) > 21:
                location = dealer.index(11)
                dealer[location] = 1

        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Dealer's first card: {dealer[0]}")

        while True:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                player.append(deal())
                if 11 in player and sum(player) > 21:
                    location = player.index(11)
                    player[location] = 1

                print(f"\nYour cards: {player}, current score: {sum(player)}")
                print(f"Dealer's first card: {dealer[0]}\n")

                if sum(player) > 21:
                    print("Your went over 21. You lose.\n")
                    break

            else:
                while sum(dealer) < 17:
                    dealer.append(deal())
                    if 11 in dealer and sum(dealer) > 21:
                        location = dealer.index(11)
                        dealer[location] = 1
                    if sum(dealer) > 21:
                        break

                if (sum(dealer) < sum(player) <= 21) or (sum(dealer) > 21):
                    print(f"\nYour final hand: {player}, final score: {sum(player)}")
                    print(f"Dealer's final card: {dealer}, final score: {sum(dealer)}")
                    print("You win!!!\n")
                    break
                elif sum(player) < sum(dealer) <= 21:
                    print(f"\nYour final hand: {player}, final score: {sum(player)}")
                    print(f"Dealer's final card: {dealer}, final score: {sum(dealer)}")
                    print("You lose!!!\n")
                    break

                else:
                    print(f"\nYour final hand: {player}, final score: {sum(player)}")
                    print(f"Dealer's final card: {dealer}, final score: {sum(dealer)}")
                    print("draw\n")
                    break
        player.clear()
        dealer.clear()
