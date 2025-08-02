
def exchange_money(budget, exchange_rate):
    return float(budget) / float(exchange_rate)

def get_change(budget, exchanging_value):
    return float(budget) - float(exchanging_value)

def get_value_of_bills(denomination, number_of_bills):
    return float(denomination) * int(number_of_bills)

def get_number_of_bills(amount, denomination):
    return int(amount) // int(denomination)
 

def get_leftover_of_bills(amount, denomination):
    return float(amount) % float(denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    final_exchange_rate = exchange_rate + ((exchange_rate * spread) / 100)
    amount = exchange_money(budget,final_exchange_rate)
    leftover_amount = get_leftover_of_bills(amount,denomination)
    return int(amount - leftover_amount)
    















    