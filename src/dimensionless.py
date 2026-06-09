def calculateReynolds(density, velocity, characteristicLength, dynamicViscosity):
    return density * velocity * characteristicLength / dynamicViscosity

def calculatePrandtl(dynamicViscosity, specificHeat, conductivity):
    return dynamicViscosity * specificHeat / conductivity

def calculateGrashof(temperatures, characteristicLength, dynamicViscosity, density, g=9.81):
        kinematicViscosity = dynamicViscosity / density
        if "surface 2" in temperatures:
            meanTemperature = temperatures["mean"]
            surface1Temperature = temperatures["surface 1"]
            surface2Temperature = temperatures["surface 2"]
            beta = 1 / (meanTemperature + 273.15)
            return g * beta * abs(surface1Temperature - surface2Temperature) * characteristicLength**3 / kinematicViscosity**2
        else:
            filmTemperature = temperatures["film"]
            fluidTemperature = temperatures["fluid"]
            surfaceTemperature = temperatures["surface"]
            beta = 1 / (filmTemperature + 273.15)
            return g * beta * abs(surfaceTemperature - fluidTemperature) * characteristicLength**3 / kinematicViscosity**2

def calculateRayleigh(grashof, prandtl):
    
    return grashof * prandtl