package lasagnamaster

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, avgtime int) int {
    if avgtime == 0 {
        return len(layers) * 2
    }
    return len(layers) * avgtime
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (noodles int, sauce float64) {
    for _, v := range layers {
        if v == "noodles" {
            noodles += 50
        } else if v == "sauce" {
            sauce += 0.2
        }
    }
    return
}
// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendlist []string, mylist []string) []string {
    sec := friendlist[len(friendlist)-1]
    mylist[len(mylist)-1] = sec
    return mylist
}
// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, portion int) []float64 {
    newSlice := append([]float64{}, quantities...)
    for i, v := range newSlice {
        newSlice[i] = (v/2) * float64(portion)
    }
    return newSlice
}
// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
