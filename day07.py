FILE = "input.txt"


if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]

        def get_level(hand):
            if any(hand.count(c) == 5 for c in cards):
                return 7
            if any(hand.count(c) == 4 for c in cards):
                return 6
            if any(hand.count(c) == 3 for c in cards) and any(hand.count(c) == 2 for c in cards):
                return 5
            if any(hand.count(c) == 3 for c in cards):
                return 4
            if sum(hand.count(c) == 2 for c in cards) == 2:
                return 3
            if any(hand.count(c) == 2 for c in cards):
                return 2
            return 1
        
        hands = [((values:=line.split())[0], int(values[1]), (get_level(values[0]), int(''.join(f'{cards.index(c):02d}' for c in values[0])))) for line in file.readlines()]
        print("Part 1:", sum(hand[1] * (i+1) for i, hand in enumerate(sorted(hands, key=lambda x: x[2]))))

    # part two 
    with open(FILE) as file:
        cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]

        def get_level(hand):
            sorted_hand = sorted(set(hand.replace('J', '')), key=lambda x: hand.count(x), reverse=True)
            if len(sorted_hand) > 1:
                max_count = hand.count(sorted_hand[0])
                second_max_count = hand.count(sorted_hand[1])
                joker_count = hand.count('J')
                if max_count == 5 or max_count + joker_count == 5:
                    return 7
                if max_count == 4 or max_count + joker_count == 4:
                    return 6
                if (max_count == 3 and second_max_count == 2) or (max_count + joker_count == 3 and second_max_count == 2) or (max_count == 3 and second_max_count + joker_count == 2):
                    return 5
                if max_count == 3 or max_count + joker_count == 3:
                    return 4
                if (max_count == 2 and second_max_count == 2) or (max_count + joker_count == 2 and second_max_count == 2) or (max_count == 2 and second_max_count + joker_count == 2):
                    return 3
                if max_count == 2 or max_count + joker_count == 2:
                    return 2
                return 1
            else: 
                return 7
            
        hands = [((values:=line.split())[0], int(values[1]), (get_level(values[0]), int(''.join(f'{cards.index(c)+1:02d}' for c in values[0])))) for line in file.readlines()]
        print("Part 2:", sum(hand[1] * i for i, hand in enumerate(sorted(hands, key=lambda x: x[2]), 1)))
