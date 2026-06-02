class FluidProperties:
    def __init__(self, density, specificHeat, dynamicViscosity, conductivity, surfaceTension=None, latentHeat=None):
        self.density = density
        self.specificHeat = specificHeat
        self.dynamicViscosity = dynamicViscosity
        self.conductivity = conductivity
        self.surfaceTension = surfaceTension
        self.latentHeat = latentHeat



def getAirProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1.299 - 4.073e-3 * T + 7.362e-6 * T**2 - 5.08e-9 * T**3          
        specificHeat = (1.006 + 8.52e-6 * T + 5.33e-7 * T**2 - 4.03e-10 * T**3) * 1000
        dynamicViscosity = (17.334 + 0.0466 * T - 1.54e-5 * T**2) * 1e-6 
        conductivity = (24.399 + 0.0673 * T - 8.77e-6 * T**2) * 1e-3     

        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)

    return results


def getWaterLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1001 - 0.178 * T - 2.57e-3 * T**2
        specificHeat = (4.208 - 9.68e-4 * T + 8.26e-6 * T**2 + 1.81e-8 * T**3) * 1000
        dynamicViscosity = (1773.5 - 51.81 * T + 0.821 * T**2 - 6.966e-3 * T**3 + 2.929e-5 * T**4 - 4.77e-8 * T**5) * 1e-6
        conductivity = 0.566 + 1.81e-3 * T - 6.76e-6 * T**2
        surfaceTension = (77.167 - 0.191 * T) * 1e-3

        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)

    return results







def getFluidProperties(fluid, temperatures):
    fluidFunctions = {
        "Air": getAirProperties,
        "Water (saturated liquid)": getWaterLProperties,
        "Water (saturated vapor)": getWaterVProperties,
        "Ethylene glycol 20%": getEthylene20Properties,
        "Ethylene glycol 40%": getEthylene40Properties,
        "Propylene glycol 20%": getPropylene20Properties,
        "Propylene glycol 40%": getPropylene40Properties,
        "Thermal fluid Duratherm 600": getDuratherm600Properties,
        "Thermal fluid Duratherm LT": getDurathermLTProperties,
        "Butane (saturated liquid)": getButaneLProperties,
        "Butane (saturated vapor)": getButaneVProperties,
        "Propane (saturated liquid)": getPropaneLProperties,
        "Propane (saturated vapor)": getPropaneVProperties,
        "Carbon dioxide CO2 (saturated liquid)": getCO2LProperties,
        "Carbon dioxide CO2 (saturated vapor)": getCO2VProperties,
        "Ammonia (saturated liquid)": getAmmoniaLProperties,
        "Ammonia (saturated vapor)": getAmmoniaVProperties,
        "R-12 (saturated liquid)": getR12LProperties,
        "R-12 (saturated vapor)": getR12VProperties,
        "R-22 (saturated liquid)": getR22LProperties,
        "R-22 (saturated vapor)": getR22VProperties,
        "R-134a (saturated liquid)": getR134aLProperties,
        "R-134a (saturated vapor)": getR134aVProperties,
        "R-404A (saturated liquid)": getR404ALProperties,
        "R-404A (saturated vapor)": getR404AVProperties,
        "R-504A (saturated liquid)": getR504ALProperties,
        "R-504A (saturated vapor)": getR504AVProperties,
        "R-508B (saturated liquid)": getR508BLProperties,
        "R-508B (saturated vapor)": getR508BVProperties,
    }

    fluidFunction = fluidFunctions[fluid]

    return fluidFunction(temperatures)



