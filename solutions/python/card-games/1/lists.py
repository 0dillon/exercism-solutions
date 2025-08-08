"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return True if number in rounds else False

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    avg = card_average(hand)
    return ((hand[0]+hand[-1])/2 == avg) or (hand[len(hand)//2] == avg)

def average_even_is_average_odd(hand):
    return (sum(hand[1::2]) / len(hand[1::2])) == (sum(hand[0::2]) / len(hand[0::2]))

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand