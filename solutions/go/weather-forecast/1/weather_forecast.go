//Package weather is a package .
package weather

var (
    // CurrentCondition is a string .
	CurrentCondition string
    //CurrentLocation is a fkn string.
	CurrentLocation  string
)
//Forecast a func duh.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
