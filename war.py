import random
import time
import matplotlib.pyplot as plt

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                            '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.card_suits = {'hearts': '\u2665', 'diamonds': '\u2666', 'clubs': '\u2663', 'spades': '\u2660'}

    def __repr__(self):
        return f'{self.rank}{self.card_suits[self.suit]}'

    def compare(self, card):
        if self.card_value[self.rank] > card.card_value[card.rank]:
            return 1
        elif self.card_value[self.rank] < card.card_value[card.rank]:
            return -1
        else:
            return 0

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                      for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

def war_game():
    d = Deck()
    player_cards = []
    computer_cards = []

    # Dealing the cards
    while len(d.cards) > 0:
        player_cards.append(d.deal())
        computer_cards.append(d.deal())

    round_count = 1
    player_win_probability = []
    computer_win_probability = []
    plt.figure()
    player_line, = plt.plot(player_win_probability, label='Player Win Probability')
    computer_line, = plt.plot(computer_win_probability, label='Computer Win Probability')
    plt.legend()

    while len(player_cards) > 0 and len(computer_cards) > 0:
        pile = []
        while True and len(player_cards)>0 and len(computer_cards) > 0:
            print(player_cards)
            print(computer_cards)
            player_card = player_cards.pop(0)
            computer_card = computer_cards.pop(0)
            pile.extend([player_card, computer_card])
            print(pile)

            print(f'Round {round_count}:')
            print(f'Player: {player_card} vs Computer: {computer_card}')
            result = player_card.compare(computer_card)

            if result > 0:
                print('Player wins the round!')
                random.shuffle(pile)  # Add some entropy
                player_cards += pile  # player gets the cards
                break
            elif result < 0:
                print('Computer wins the round!')
                random.shuffle(pile)  # Add some entropy
                computer_cards += pile  # computer gets the cards
                break
            else:
                print('It is a war! Each player turns up one card face down and one card face up.')
                if len(player_cards) < 2 or len(computer_cards) < 2:
                    print('Not enough cards to continue the war. Game ends.')
                    if len(player_cards) < 2:
                        print('Computer wins')
                    else:
                        print('Player wins')
                    return
                pile.extend([player_cards.pop(0), computer_cards.pop(0)])

        print(f'Player card count: {len(player_cards)}')
        print(f'Computer card count: {len(computer_cards)}')

        total_cards = len(player_cards) + len(computer_cards)
        player_win_probability.append(len(player_cards) / total_cards)
        computer_win_probability.append(len(computer_cards) / total_cards)

        player_line.set_ydata(player_win_probability)
        player_line.set_xdata(range(len(player_win_probability)))
        computer_line.set_ydata(computer_win_probability)
        computer_line.set_xdata(range(len(computer_win_probability)))

        plt.xlim(0, len(player_win_probability))
        plt.ylim(0, 1)
        plt.draw()
        plt.pause(0.01)

        #time.sleep(0.05)
        round_count += 1

    # Checking who won the game
    if len(player_cards) > len(computer_cards):
        print('Player wins the game!')
    elif len(player_cards) < len(computer_cards):
        print('Computer wins the game!')
    else:
        print('The game is a draw!')

    plt.show()
    input("Press Enter to exit...")
    quit()

if __name__ == '__main__':
    war_game()

