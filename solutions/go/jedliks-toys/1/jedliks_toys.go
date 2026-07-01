package jedlik

import "fmt"

// type Car struct {
//     battery, distance, batteryDrain, speed int
// }

// Drive modifies the car's state, so it requires a pointer receiver (*Car).
// It also checks if there is enough battery to drive.
func (car *Car) Drive() {
	if car.battery >= car.batteryDrain {
		car.battery -= car.batteryDrain
		car.distance += car.speed
	}
}

// DisplayDistance returns the formatted distance.
func (car Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %d meters", car.distance)
}

// DisplayBattery returns the formatted battery level.
func (car Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %d%%", car.battery)
}

// CanFinish calculates if the car can travel the required track distance.
func (car Car) CanFinish(trackDistance int) bool {
    // Calculate the maximum distance the car can drive with its current battery
	maxDistance := (car.battery / car.batteryDrain) * car.speed
	return maxDistance >= trackDistance
}