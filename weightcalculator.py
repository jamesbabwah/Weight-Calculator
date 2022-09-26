class WeightCalculator:
    #Functions that accept weight on earth and return the weight to given planets
    def Mercury(weight):
        return weight * 0.38

    def Venus(weight):
        return weight * 0.91

    def Mars(weight):
        return weight * 0.38

    def Saturn(weight):
        return weight * 1.06

    def Jupiter(weight):
        return weight * 2.34

    def Uranus(weight):
        return weight * 0.92

    def Neptune(weight):
        return weight * 1.1

    def Pluto(weight):
        return weight * 0.06

#Allows code to be run only if "weightcalculator.py" is ran
#This part won't be executed if the file is imported as a module
if __name__ == '__main__':
    #Will ask for mass until an input in a numerical form is given
    astronaut_mass = 0.0
    while not astronaut_mass:
        try:
            astronaut_mass = float(input("Enter the mass of the astronaut: "))
        except ValueError:
            print("Mass must be a number")
            continue

    #Input planet to calculate weight for
    planet = input("Select a planet in the solar system: ")

    #Asks to input planet again if planet isn't one in this solar system
    valid_planets = ['saturn','jupiter','mars','mercury','venus','uranus','neptune','pluto' ]
    while planet.lower() not in valid_planets:
        planet = input('Select a planet in the solar system: ')

    #Calculate weight
    if planet.lower() == "mercury":
        result = WeightCalculator.Mercury(astronaut_mass)
    if planet.lower() == "venus":
        result = WeightCalculator.Venus(astronaut_mass)
    if planet.lower() == "mars":
        result = WeightCalculator.Mars(astronaut_mass)
    if planet.lower() == "saturn":
        result = WeightCalculator.Saturn(astronaut_mass)
    if planet.lower() == "jupiter":
        result = WeightCalculator.Jupiter(astronaut_mass)
    if planet.lower() == "uranus":
        result = WeightCalculator.Uranus(astronaut_mass)
    if planet.lower() == "neptune":
        result = WeightCalculator.Neptune(astronaut_mass)
    if planet.lower() == "pluto":
        result = WeightCalculator.Pluto(astronaut_mass)

    #Print weight
    print("your weight on the planet is: ", result)