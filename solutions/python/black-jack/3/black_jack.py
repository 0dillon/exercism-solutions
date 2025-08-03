
def value_of_card(card):   
    if card in "KJQ":
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    return card_two

def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) < 11:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    return (card_one == "A" and value_of_card(card_two) == 10) or (value_of_card(card_one) == 10 and card_two == "A")
        

def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) < 9:
        return False
    if value_of_card(card_one) + value_of_card(card_two) > 11:
        return False
    return True
    
