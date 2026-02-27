package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
        case "ace" :
        return 11
        case "two":
        return 2
        case "three":
        return 3
        case "four":
        return 4
        case "five":
        return 5
        case "six":
        return 6
        case "seven":
        return 7
        case "eight":
        return 8
        case "nine":
        return 9
        case "ten", "jack", "queen", "king":
        return 10
        default :
        return 0
    }
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
    h1 := ParseCard(card1)
    h2 := ParseCard(card2)
    deal := ParseCard(dealerCard)
    hand := h1 + h2
	switch {
        case h1 == 11 && h2 == 11:
        return "P"
        case hand == 21 && deal != 10 && deal != 11:
        return "W"
        case hand == 21 && deal >= 10 :
        return "S"
        case hand >= 17 && hand < 21 :
        return "S"
        case hand >= 12 && hand < 17 && deal >= 7 :
        return "H"
        case hand >= 12 && hand < 17 :
        return "S"
        case hand >= 11 :
        return "H"
        default :
        return "H"
    }
}
