class WeightCalculator:
    valid_planets = ['saturn','jupiter','mars','mercury','venus','uranus','neptune','pluto' ]

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

    #Calulates weight given a mass and a planet
    def calculate(mass, planet):
        if planet.lower() == "mercury":
            return WeightCalculator.Mercury(mass)
        if planet.lower() == "venus":
            return WeightCalculator.Venus(mass)
        if planet.lower() == "mars":
            return WeightCalculator.Mars(mass)
        if planet.lower() == "saturn":
            return WeightCalculator.Saturn(mass)
        if planet.lower() == "jupiter":
            return WeightCalculator.Jupiter(mass)
        if planet.lower() == "uranus":
            return WeightCalculator.Uranus(mass)
        if planet.lower() == "neptune":
            return WeightCalculator.Neptune(mass)
        if planet.lower() == "pluto":
            return WeightCalculator.Pluto(mass)
        
        #if planet isn't one in this solar system or earth
        raise ValueError("Planet must be one from our solar system except earth")

#Allows code to be run only if "weightcalculator.py" is ran
#This part won't be executed if the file is imported as a module
if __name__ == '__main__':
    #Will ask for mass until an input in a numerical form is given
    astronaut_mass = 0.0
    while not astronaut_mass:
        try:
            astronaut_mass = float(input("Enter the mass of the astronaut: ")) #nothing will be assigned if ValueError is raised therefore astronaut_mass will evaluate to false
        except ValueError:
            print("Mass must be a number")
            continue

    #Input planet to calculate weight for
    planet = input("Select a planet in the solar system: ")

    #Asks to input planet again if planet isn't one in this solar system (or earth)
    while planet.lower() not in WeightCalculator.valid_planets:
        planet = input('Select a planet in the solar system: ')

    #Calculate weight
    result = WeightCalculator.calculate(astronaut_mass, planet)

    #Print weight to two decimal places
    print(f"your weight on the planet is: {result:.2f}")