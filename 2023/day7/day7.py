from enum import Enum
from functools import cmp_to_key

card_strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
#card_strengths_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
input_file = "input.txt"


def parse_file(file):
    with open(file) as file:
        lines = file.readlines()
    file_contents = []
    for line in lines:
        cards = line.split()[0].strip()
        bid = int(line.split()[1].strip())
        file_contents.append(Line(cards, bid))
    return file_contents


# PART ONE
def evaluate_card(card):
    return card_strengths.index(card)


#def evaluate_card_2(card):
#    return card_strengths_2.index(card)


class Comparison(Enum):
    STRONGER = 1
    EQUAL = 2
    WEAKER = 3


def compare_card(card1, card2):
    strength1, strength2 = evaluate_card(card1), evaluate_card(card2)
    if strength1 < strength2:
        return 1
    elif strength1 == strength2:
        return 0
    else:
        return -1


#def compare_card_2(card1, card2):
#    strength1, strength2 = evaluate_card_2(card1), evaluate_card_2(card2)
#    if strength1 < strength2:
#        return 1
#    elif strength1 == strength2:
#        return 0
#    else:
#        return -1


class HandPattern(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


def evaluate_pattern(pattern):
    return pattern.value


def comparePattern(pattern1, pattern2):
    strength1, strength2 = evaluate_pattern(pattern1), evaluate_pattern(pattern2)
    if strength1 < strength2:
        return 1
    elif strength1 == strength2:
        return 0
    else:
        return -1


class Line:
    def __init__(self, hand, bid):
        self.hand = Hand(hand)
        self.bid = int(bid)

    def __repr__(self):
        return str(self.bid) + " " + str(self.hand)

    def evaluateStrength(self):
        return self.hand.evaluateStrength()


class Hand:
    def __init__(self, cards):
        assert (len(cards) == 5)
        self.interesting_cards = []  # interesting cards are not quite necessary (yet)
        self.pattern = None
        self.original_cards = list(cards)
        self.cards = list(sorted(cards))

    def __repr__(self):
        return "".join(self.original_cards)

    def evaluatePattern(self):
        # five of a kind
        if all(x == self.cards[0] for x in self.cards):
            self.interesting_cards = [self.cards[0]]
            self.pattern = HandPattern.FIVE_OF_A_KIND
            return
        # four of a kind
        elif (self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2] and self.cards[0] == self.cards[3]) or (
                self.cards[1] == self.cards[2] and self.cards[1] == self.cards[3] and self.cards[1] == self.cards[4]):
            self.interesting_cards = [self.cards[2]]
            self.pattern = HandPattern.FOUR_OF_A_KIND
            return
        # full house
        elif self.cards[0] == self.cards[1] and self.cards[2] == self.cards[3] and self.cards[2] == self.cards[4]:
            self.interesting_cards = [self.cards[2], self.cards[0]]
            self.pattern = HandPattern.FULL_HOUSE
            return
        elif self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2] and self.cards[3] == self.cards[4]:
            self.interesting_cards = [self.cards[0], self.cards[3]]
            self.pattern = HandPattern.FULL_HOUSE
            return
        # three of a kind
        elif (self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2]) or (
                self.cards[1] == self.cards[2] and self.cards[1] == self.cards[3]) or (
                self.cards[2] == self.cards[3] and self.cards[3] == self.cards[4]):
            self.interesting_cards = [self.cards[2]]
            self.pattern = HandPattern.THREE_OF_A_KIND
            return
        # two pair
        elif self.cards[0] == self.cards[1] and self.cards[2] == self.cards[3]:
            self.interesting_cards = [self.cards[0], self.cards[2]]
            self.pattern = HandPattern.TWO_PAIR
            return
        elif self.cards[0] == self.cards[1] and self.cards[3] == self.cards[4]:
            self.interesting_cards = [self.cards[0], self.cards[3]]
            self.pattern = HandPattern.TWO_PAIR
            return
        elif self.cards[1] == self.cards[2] and self.cards[3] == self.cards[4]:
            self.interesting_cards = [self.cards[1], self.cards[3]]
            self.pattern = HandPattern.TWO_PAIR
            return
        # one pair
        elif self.cards[0] == self.cards[1]:
            self.interesting_cards = [self.cards[0]]
            self.pattern = HandPattern.ONE_PAIR
            return
        elif self.cards[1] == self.cards[2]:
            self.interesting_cards = [self.cards[1]]
            self.pattern = HandPattern.ONE_PAIR
            return
        elif self.cards[2] == self.cards[3]:
            self.interesting_cards = [self.cards[2]]
            self.pattern = HandPattern.ONE_PAIR
            return
        elif self.cards[3] == self.cards[4]:
            self.interesting_cards = [self.cards[3]]
            self.pattern = HandPattern.ONE_PAIR
            return
        # high card
        else:
            self.interesting_cards = min(self.cards, key=lambda x: evaluate_card(x))
            self.pattern = HandPattern.HIGH_CARD
            return

    def evaluateStrength(self):
        self.evaluatePattern()
        return self.pattern, self.original_cards

    #def evaluateStrength_2(self):
    #    self.upgrade()
    #    self.evaluatePattern()
    #    return self.pattern, self.original_cards

    #def hasJoker(self):
    #    return "J" in self.cards

    #def upgrade(self):
    #    if self.hasJoker():
    #        self.evaluatePattern()
    #        # upgrade high card to one pair
    #        if self.pattern == HandPattern.HIGH_CARD:
    #            self.upgradeHighCard()
    #            return
    #        elif self.pattern == HandPattern.ONE_PAIR:
    #            self.upgradeOnePair()
    #    else:
    #        return

    #def upgradeHighCard(self):
    #    # find highest card
    #    highest = self.cards[4]
    #    index = self.original_cards.index(highest)
    #    if index == 0:
    #        self.original_cards[1] = highest
    #        self.cards = sorted(self.original_cards)
    #    else:
    #        self.original_cards[0] = highest
    #        self.cards = sorted(self.original_cards)
    #    return

    #def upgradeOnePair(self):



def compare_hand_cards(cards1, cards2):
    for (card1, card2) in zip(cards1, cards2):
        if compare_card(card1, card2) != 0:
            return compare_card(card1, card2)
    return compare_card(cards1[4], cards2[4])


#def compare_hand_cards_2(cards1, cards2):
#    for (card1, card2) in zip(cards1, cards2):
#        if compare_card_2(card1, card2) != 0:
#            return compare_card_2(card1, card2)
#    return compare_card_2(cards1[4], cards2[4])


def compare_hands(hand1, hand2):
    pattern1, cards1 = hand1.evaluateStrength()
    pattern2, cards2 = hand2.evaluateStrength()
    if comparePattern(pattern1, pattern2) != 0:
        return comparePattern(pattern1, pattern2)
    else:
        return compare_hand_cards(cards1, cards2)


#def compare_hands_2(hand1, hand2):
#    pattern1, cards1 = hand1.evaluateStrength()
#    pattern2, cards2 = hand2.evaluateStrength()
#    if comparePattern(pattern1, pattern2) != 0:
#        return comparePattern(pattern1, pattern2)
#    else:
#        return compare_hand_cards_2(cards1, cards2)


file_contents = parse_file(input_file)

cards_bids_sorted = sorted(file_contents, key=cmp_to_key(compare_hands))

results = []
for index, line in enumerate(cards_bids_sorted):
    bid = line.bid
    rank = index + 1
    results.append(rank * bid)

print("Answer for Part One is: ", sum(results))

# PART TWO
#test_hand_1 = Hand("32T3K")
#test_hand_2 = Hand("2345J")
#print(test_hand_2.evaluateStrength())
#print(test_hand_2.evaluateStrength_2())

