import re

FILE = "input.txt"

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        cards = [[re.findall('\d+', part) for part in line.split(':')[1].split('|')] for line in file.readlines()]
        print("Part 1:", sum(2**(len([*filter(lambda x: x in card[0], card[1])])-1) for card in cards if len([*filter(lambda x: x in card[0], card[1])]) > 0))

    # part two 
    with open(FILE) as file:
        cards = [[re.findall('\d+', part) for part in line.split(':')[1].split('|')] for line in file.readlines()]
        card_indeces = [*range(len(cards))]
        cards_to_won_cards = {i: [*range(i+1,i+1+len([*filter(lambda x: x in card[0], card[1])]))] for i, card in enumerate(cards)}
        for i, card in cards_to_won_cards.items():
            card_indeces += card*card_indeces.count(i)
        print("Part 2:", len(card_indeces))
