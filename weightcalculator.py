class WeightCalculator:
    #Functions that accept weight on earth and return the weight to given planets
    def Mercury(weight: float | int) -> float:
        return weight * 0.38

    def Venus(weight: float | int) -> float:
        return weight * 0.91

    def Mars(weight: float | int) -> float:
        return weight * 0.38

    def Saturn(weight: float | int) -> float:
        return weight * 1.06

    def Jupiter(weight: float | int) -> float:
        return weight * 2.34

    def Uranus(weight: float | int) -> float:
        return weight * 0.92

    def Neptune(weight: float | int) -> float:
        return weight * 1.1

    def Pluto(weight: float | int) -> float:
        return weight * 0.06

#Allows code to be run only if "weightcalculator.py" is ran
#This part won't be executed if the file is imported as a module
if __name__ == '__main__':
    #Input weight
    astronaut_mass: float = 0.0
    while not astronaut_mass:
        try:
            astronaut_mass = float(input("Enter the mass of the astronaut: "))
        except ValueError:
            print("Mass must be a number")
            continue

    #Input planet to calculate weight for
    planet: str = input("Select a planet in the solar system: ")
    valid_planets : list[str] = ['saturn','jupiter','mars','mercury','venus','uranus','neptune','pluto' ]
    while planet.lower() not in valid_planets:
        planet = input('Select a planet in the solar system: ')

    #Calculate weight
    if planet.lower() == "mercury":
        result: float = WeightCalculator.Mercury(astronaut_mass)
    if planet.lower() == "venus":
        result: float = WeightCalculator.Venus(astronaut_mass)
    if planet.lower() == "mars":
        result: float = WeightCalculator.Mars(astronaut_mass)
    if planet.lower() == "saturn":
        result: float = WeightCalculator.Saturn(astronaut_mass)
    if planet.lower() == "jupiter":
        result: float = WeightCalculator.Jupiter(astronaut_mass)
    if planet.lower() == "uranus":
        result: float = WeightCalculator.Uranus(astronaut_mass)
    if planet.lower() == "neptune":
        result: float = WeightCalculator.Neptune(astronaut_mass)
    if planet.lower() == "pluto":
        result: float = WeightCalculator.Pluto(astronaut_mass)

    #Print weight
    print(f"your weight on {planet} is: {result:.2f}")