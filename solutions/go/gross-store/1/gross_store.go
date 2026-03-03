package gross

// Units stores the Gross Store unit measurements.
func Units() map[string]int {
	measurement := map[string]int{
        "quarter_of_a_dozen": 3,
        "half_of_a_dozen": 6,
        "dozen": 12,
        "small_gross": 120,
        "gross": 144,
        "great_gross": 1728,
    }
    return measurement
}

// NewBill creates a new bill.
func NewBill() map[string]int {
	return make(map[string]int)
 
}

// AddItem adds an item to customer bill.
func AddItem(bill, units map[string]int, item, unit string) bool {
	amount, exist := units[unit]
    if !exist {
        return false
    }
    bill[item] += amount
    return true
}

// RemoveItem removes an item from customer bill.
func RemoveItem(bill, units map[string]int, item, unit string) bool {
	currentQty, itemExists := bill[item]
	if !itemExists {
		return false
	}
	unitValue, unitExists := units[unit]
	if !unitExists {
		return false
	}
	newQty := currentQty - unitValue
	if newQty < 0 {
		return false
	}
	if newQty == 0 {
		delete(bill, item)
		return true
	}
	bill[item] = newQty
	return true
}

// GetItem returns the quantity of an item that the customer has in his/her bill.
func GetItem(bill map[string]int, item string) (int, bool) {
	qty, exists := bill[item]
	return qty, exists
}