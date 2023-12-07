from enum import Enum
from functools import cmp_to_key

card_strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_strengths_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
input_file = "input.txt"

# WANTED RESULTS FOR TEST FILES
#  test_input.txt    1) 6440 2) 5905
#  test_input_2.txt  1) 6592 2) 6839


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


def evaluate_card_2(card):
    return card_strengths_2.index(card)


def compare_card(card1, card2):
    strength1, strength2 = evaluate_card(card1), evaluate_card(card2)
    if strength1 < strength2:
        return 1
    elif strength1 == strength2:
        return 0
    else:
        return -1


def compare_card_2(card1, card2):
    strength1, strength2 = evaluate_card_2(card1), evaluate_card_2(card2)
    if strength1 < strength2:
        return 1
    elif strength1 == strength2:
        return 0
    else:
        return -1


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

    def evaluate_strength(self):
        return self.hand.evaluate_strength()

    def evaluate_strength_2(self):
        return self.hand.evaluate_strength_2()


class Hand:
    def __init__(self, cards):
        assert (len(cards) == 5)
        self.interesting_cards = []  # interesting cards are not quite necessary (yet)
        self.pattern = None
        self.patternIgnoreJokers = None
        self.original_cards = list(cards)
        self.cards = list(sorted(cards))
        self.upgraded_cards = list(cards)

    def __repr__(self):
        return "".join(self.original_cards)

    def find_indices(self, item_to_find):
        return [idx for idx, value in enumerate(self.original_cards) if value == item_to_find]

    def get_highest_card(self):
        highest = "J"
        for card in self.cards:
            if card_strengths_2.index(card) < card_strengths_2.index(highest):
                highest = card
        return highest

    def evaluate_pattern(self, cards):
        cards = sorted(cards)
        # five of a kind
        if all(x == cards[0] for x in cards):
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.pattern = HandPattern.FIVE_OF_A_KIND
            return
        # four of a kind
        elif cards[0] == cards[1] and cards[0] == cards[2] and cards[0] == cards[3]:
            self.interesting_cards = self.find_indices(self.cards[0])
            self.pattern = HandPattern.FOUR_OF_A_KIND
            return
        elif cards[1] == cards[2] and cards[1] == cards[3] and cards[1] == cards[4]:
            self.interesting_cards = self.find_indices(self.cards[1])
            self.pattern = HandPattern.FOUR_OF_A_KIND
            return
        # full house
        elif cards[0] == cards[1] and cards[2] == cards[3] and cards[2] == cards[4]:
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.pattern = HandPattern.FULL_HOUSE
            return
        elif cards[0] == cards[1] and cards[0] == cards[2] and cards[3] == cards[4]:
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.pattern = HandPattern.FULL_HOUSE
            return
        # three of a kind
        elif (cards[0] == cards[1] and cards[0] == cards[2]) or (
                cards[1] == cards[2] and cards[1] == cards[3]) or (
                cards[2] == cards[3] and cards[3] == cards[4]):
            self.interesting_cards = self.find_indices(cards[3])
            self.pattern = HandPattern.THREE_OF_A_KIND
            return
        # two pair
        elif cards[0] == cards[1] and cards[2] == cards[3]:
            self.interesting_cards = self.find_indices(cards[0]) + self.find_indices(cards[2])
            self.pattern = HandPattern.TWO_PAIR
            return
        elif cards[0] == cards[1] and cards[3] == cards[4]:
            self.interesting_cards = self.find_indices(cards[0]) + self.find_indices(cards[3])
            self.pattern = HandPattern.TWO_PAIR
            return
        elif cards[1] == cards[2] and cards[3] == cards[4]:
            self.interesting_cards = self.find_indices(cards[1]) + self.find_indices(cards[3])
            self.pattern = HandPattern.TWO_PAIR
            return
        # one pair
        elif cards[0] == cards[1]:
            self.interesting_cards = self.find_indices(cards[0])
            self.pattern = HandPattern.ONE_PAIR
            return
        elif cards[1] == cards[2]:
            self.interesting_cards = self.find_indices(cards[1])
            self.pattern = HandPattern.ONE_PAIR
            return
        elif cards[2] == cards[3]:
            self.interesting_cards = self.find_indices(cards[2])
            self.pattern = HandPattern.ONE_PAIR
            return
        elif cards[3] == cards[4]:
            self.interesting_cards = self.find_indices(cards[3])
            self.pattern = HandPattern.ONE_PAIR
            return
        # high card
        else:
            self.interesting_cards = min(cards, key=lambda x: evaluate_card(x))
            self.pattern = HandPattern.HIGH_CARD
            return

    def evaluate_pattern_ignore_jokers(self):
        # five of a kind
        if all(x == self.cards[0] for x in self.cards) and self.cards[0] != "J":
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.patternIgnoreJokers = HandPattern.FIVE_OF_A_KIND
            return
        # four of a kind
        elif (self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2] and self.cards[0] == self.cards[3] and
              self.cards[0] != "J") or (
                self.cards[1] == self.cards[2] and self.cards[1] == self.cards[3] and self.cards[1] == self.cards[4] and
                self.cards[1] != "J"):
            self.interesting_cards = self.find_indices(self.cards[1])
            self.patternIgnoreJokers = HandPattern.FOUR_OF_A_KIND
            return
        # full house
        elif self.cards[0] == self.cards[1] and self.cards[0] != "J" and self.cards[2] == self.cards[3] and self.cards[
            2] == self.cards[4] and self.cards[2] != "J":
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.patternIgnoreJokers = HandPattern.FULL_HOUSE
            return
        elif self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2] and self.cards[0] != "J" and self.cards[
            3] == self.cards[4] and self.cards[3] != "J":
            self.interesting_cards = [0, 1, 2, 3, 4]
            self.patternIgnoreJokers = HandPattern.FULL_HOUSE
            return
        # three of a kind
        elif ((self.cards[0] == self.cards[1] and self.cards[0] == self.cards[2]) or (
                self.cards[1] == self.cards[2] and self.cards[1] == self.cards[3]) or (
                      self.cards[2] == self.cards[3] and self.cards[3] == self.cards[4])) and self.cards[2] != "J":
            self.interesting_cards = self.find_indices(self.cards[3])
            self.patternIgnoreJokers = HandPattern.THREE_OF_A_KIND
            return
        # two pair
        elif self.cards[0] == self.cards[1] and self.cards[2] == self.cards[3] and self.cards[0] != "J" and self.cards[
            2] != "J":
            self.interesting_cards = self.find_indices(self.cards[0]) + self.find_indices(self.cards[2])
            self.patternIgnoreJokers = HandPattern.TWO_PAIR
            return
        elif self.cards[0] == self.cards[1] and self.cards[3] == self.cards[4] and self.cards[0] != "J" and self.cards[
            3] != "J":
            self.interesting_cards = self.find_indices(self.cards[0]) + self.find_indices(self.cards[3])
            self.patternIgnoreJokers = HandPattern.TWO_PAIR
            return
        elif self.cards[1] == self.cards[2] and self.cards[3] == self.cards[4] and self.cards[1] != "J" and self.cards[
            3] != "J":
            self.interesting_cards = self.find_indices(self.cards[1]) + self.find_indices(self.cards[3])
            self.patternIgnoreJokers = HandPattern.TWO_PAIR
            return
        # one pair
        elif self.cards[0] == self.cards[1] and self.cards[0] != "J":
            self.interesting_cards = self.find_indices(self.cards[0])
            self.patternIgnoreJokers = HandPattern.ONE_PAIR
            return
        elif self.cards[1] == self.cards[2] and self.cards[1] != "J":
            self.interesting_cards = self.find_indices(self.cards[1])
            self.patternIgnoreJokers = HandPattern.ONE_PAIR
            return
        elif self.cards[2] == self.cards[3] and self.cards[2] != "J":
            self.interesting_cards = self.find_indices(self.cards[2])
            self.patternIgnoreJokers = HandPattern.ONE_PAIR
            return
        elif self.cards[3] == self.cards[4] and self.cards[3] != "J":
            self.interesting_cards = self.find_indices(self.cards[3])
            self.patternIgnoreJokers = HandPattern.ONE_PAIR
            return
        # high card
        else:
            self.interesting_cards = self.find_indices(min(self.cards, key=lambda x: evaluate_card(x)))
            #assert(len(self.interesting_cards) == 1)
            self.patternIgnoreJokers = HandPattern.HIGH_CARD
            return

    def evaluate_strength(self):
        self.evaluate_pattern(self.cards)
        return self.pattern, self.original_cards

    def evaluate_strength_2(self):
        self.upgrade()
        #print("got here")
        self.evaluate_pattern(self.upgraded_cards)
        return self.pattern, self.original_cards

    def has_joker(self):
        return "J" in self.upgraded_cards

    def upgrade(self):
        if self.has_joker():
            while self.has_joker():
                if self.upgraded_cards == ["J", "J", "J", "J", "J"]:
                    self.upgraded_cards = ["A", "A", "A", "A", "A"]
                    return
                else:
                    self.evaluate_pattern_ignore_jokers()
                    # upgrade high card to one pair
                    if self.patternIgnoreJokers == HandPattern.HIGH_CARD:
                        self.upgrade_high_card()
                        #return
                    elif self.patternIgnoreJokers == HandPattern.ONE_PAIR:
                        self.upgrade_one_pair()
                        #return
                    elif self.patternIgnoreJokers == HandPattern.TWO_PAIR:
                        self.upgrade_two_pairs()
                        #return
                    elif self.patternIgnoreJokers == HandPattern.THREE_OF_A_KIND:
                        self.upgrade_three_of_a_kind()
                        #return
                    elif self.patternIgnoreJokers == HandPattern.FOUR_OF_A_KIND:
                        self.upgrade_four_of_a_kind()
                        #return
            return

    def upgrade_high_card(self):
        # find highest card
        highest = self.get_highest_card()
        joker_index = self.upgraded_cards.index("J")
        if highest == "J":
            highest = self.cards[3]
            if highest == "J":
                highest = self.cards[2]
                if highest == "J":
                    highest = self.cards[1]
                    if highest == "J":
                        highest = self.cards[0]
        self.upgraded_cards[joker_index] = highest
        return

    def upgrade_one_pair(self):
        double = self.original_cards[self.interesting_cards[0]]
        assert(double != "J")
        joker_index = self.upgraded_cards.index("J")
        # print("replacing J at index ", joker_index, " with ", double)
        self.upgraded_cards[joker_index] = double
        return

    def upgrade_two_pairs(self):
        doubles = [number for number in self.cards if self.cards.count(number) == 2]
        joker_index = self.upgraded_cards.index("J")
        #print("replacing J at index ", joker_index, " with ", to_be_upgraded)
        self.upgraded_cards[joker_index] = max(doubles)
        return

    def upgrade_three_of_a_kind(self):
        triple = [number for number in self.cards if self.cards.count(number) == 3][0]
        joker_index = self.upgraded_cards.index("J")
        # print("replacing J at index ", joker_index, " with ", triple)
        self.upgraded_cards[joker_index] = triple
        return

    def upgrade_four_of_a_kind(self):
        quadruple = [number for number in self.cards if self.cards.count(number) == 4][0]
        joker_index = self.upgraded_cards.index("J")
        # print("replacing J at index ", joker_index, " with ", quadruple)
        self.upgraded_cards[joker_index] = quadruple
        return


def compare_hand_cards(cards1, cards2):
    for (card1, card2) in zip(cards1, cards2):
        if compare_card(card1, card2) != 0:
            return compare_card(card1, card2)
    return compare_card(cards1[4], cards2[4])


def compare_hand_cards_2(cards1, cards2):
    for (card1, card2) in zip(cards1, cards2):
        if compare_card_2(card1, card2) != 0:
            return compare_card_2(card1, card2)
    return compare_card_2(cards1[4], cards2[4])


def compare_hands(hand1, hand2):
    pattern1, cards1 = hand1.evaluate_strength()
    pattern2, cards2 = hand2.evaluate_strength()
    if comparePattern(pattern1, pattern2) != 0:
        return comparePattern(pattern1, pattern2)
    else:
        return compare_hand_cards(cards1, cards2)


def compare_hands_2(hand1, hand2):
    # print("comparing ", hand1, hand2)
    pattern1, cards1 = hand1.evaluate_strength_2()
    pattern2, cards2 = hand2.evaluate_strength_2()
    comparison_result = comparePattern(pattern1, pattern2)
    if comparison_result != 0:
        #print("compared hand ", "".join(cards1), " and hand ", "".join(cards2), " and got ", comparison_result)
        return comparison_result
    else:
        return compare_hand_cards_2(cards1, cards2)


file_contents = parse_file(input_file)

cards_bids_sorted = sorted(file_contents, key=cmp_to_key(compare_hands))
#print(cards_bids_sorted)

results = []
for index, line in enumerate(cards_bids_sorted):
    bid = line.bid
    rank = index + 1
    results.append(rank * bid)

print("Answer for Part One is: ", sum(results))

# PART TWO
debug = False
if debug:
    test1 = Hand("KTJJT")
    test2 = Hand("T3Q33")
    print(test1.evaluate_strength_2())
    print(test2.evaluate_strength_2())
    print(compare_hands_2(test1, test2))

else:
    cards_bids_sorted_new = sorted(file_contents, key=cmp_to_key(compare_hands_2))
    #print(cards_bids_sorted_new)

    results = []
    for index, line in enumerate(cards_bids_sorted_new):
        bid = line.bid
        rank = index + 1
        #print(rank, bid, "".join(line.hand.original_cards))
        results.append(rank * bid)

    print("Answer for Part Two is: ", sum(results))