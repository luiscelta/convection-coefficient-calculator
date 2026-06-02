class FluidProperties:
    def __init__(self, density, specificHeat, dynamicViscosity, conductivity, surfaceTension=None, latentHeat=None):
        self.density = density
        self.specificHeat = specificHeat
        self.dynamicViscosity = dynamicViscosity
        self.conductivity = conductivity
        self.surfaceTension = surfaceTension
        self.latentHeat = latentHeat


# Air
def getAirProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1.299 - 4.073e-3 * T + 7.362e-6 * T**2 - 5.08e-9 * T**3          
        specificHeat = (1.006 + 8.52e-6 * T + 5.33e-7 * T**2 - 4.03e-10 * T**3) * 1000
        dynamicViscosity = (17.334 + 0.0466 * T - 1.54e-5 * T**2) * 1e-6 
        conductivity = (24.399 + 0.0673 * T - 8.77e-6 * T**2) * 1e-3     
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results

# Water (saturated liquid)
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

# Water (saturated vapor)
def getWaterVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = -0.379 + 0.0193 * T - 3.39e-4 * T**2 + 3.17e-6 * T**3 - 1.01e-8 * T**4 + 2.71e-11 * T**5
        specificHeat = (1.855 + 2.09e-3 * T - 1.41e-5 * T**2 + 1.6e-7 * T**3) * 1000
        dynamicViscosity = (8.951 + 0.0327 * T + 5.77e-6 * T**2) * 1e-6
        conductivity = (18.15 + 0.0266 * T + 4.19e-4 * T**2) * 1e-3
        latentHeat = (2456.6 - 1.31 * T - 6.49e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# Ethylene glycol 20%
def getEthylene20Properties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1035.7 - 0.248 * T - 2.44e-3 * T**2
        specificHeat = (3.769 + 2.3e-3 * T) * 1000
        dynamicViscosity = (3029 - 109 * T + 2.68 * T**2 - 0.0399 * T**3 + 2.51e-4 * T**4) * 1e-6
        conductivity = 0.468 + 1.58e-3 * T - 7.02e-6 * T**2
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Ethylene glycol 40%
def getEthylene40Properties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1066.8 - 0.307 * T - 2.44e-3 * T**2
        specificHeat = (3.401 + 3.35e-3 * T) * 1000
        dynamicViscosity = (5753 - 230 * T + 8 * T**2 - 0.216 * T**3 + 2.46e-3 * T**4) * 1e-6
        conductivity = 0.395 + 1.1e-3 * T - 4.54e-6 * T**2
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Propylene glycol 20%
def getPropylene20Properties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1025.8 - 0.291 * T - 2.51e-3 * T**2
        specificHeat = (3.929 + 2.18e-3 * T) * 1000
        dynamicViscosity = (4060 - 162 * T + 3.96 * T**2 - 0.0564 * T**3 + 3.4e-4 * T**4) * 1e-6
        conductivity = 0.464 + 1.51e-3 * T - 7.1e-6 * T**2
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Propylene glycol 40%
def getPropylene40Properties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1045.1 - 0.392 * T - 2.57e-3 * T**2
        specificHeat = (3.636 + 3.3e-3 * T) * 1000
        dynamicViscosity = (12245 - 751 * T + 30.3 * T**2 - 0.711 * T**3 + 6.58e-3 * T**4) * 1e-6
        conductivity = 0.385 + 9.54e-4 * T - 4.84e-6 * T**2
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Duratherm 600
def getDuratherm600Properties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 869.1 - 0.672 * T
        specificHeat = (1.843 + 3.27e-3 * T) * 1000
        dynamicViscosity = 6.63e7 * T**(-2.07) * 1e-6
        conductivity = 0.144 - 5.16e-5 * T
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Duratherm LT
def getDurathermLTProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 826.9 - 0.68 * T
        specificHeat = (2.02 + 3.44e-3 * T) * 1000
        dynamicViscosity = 1.9311e6 * T**(-1.53) * 1e-6
        conductivity = 0.143 - 8.57e-5 * T
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity)
    return results


# Butane (saturated liquid)
def getButaneLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 600.8 - 1.09 * T - 1.57e-3 * T**2
        specificHeat = (2.3 + 4.76e-3 * T + 2.08e-5 * T**2 + 3.39e-8 * T**3) * 1000
        dynamicViscosity = (202.1 - 2.06 * T + 0.0154 * T**2 - 1.06e-4 * T**3) * 1e-6
        conductivity = 0.1154 - 4.36e-4 * T + 5e-7 * T**2
        surfaceTension = (14.92 - 0.123 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# Butane (saturated vapor)
def getButaneVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 2.748 + 0.0974 * T + 1.4e-3 * T**2 + 8.84e-6 * T**3
        specificHeat = (1.653 + 5.85e-3 * T + 2.14e-5 * T**2 + 5.94e-8 * T**3) * 1000
        dynamicViscosity = (6.767 + 0.0249 * T + 1.71e-5 * T**2) * 1e-6
        conductivity = (14.184 + 0.0919 * T + 2.22e-4 * T**2) * 1e-3
        latentHeat = (384.5 - 0.904 * T - 2.14e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# Propane (saturated liquid)
def getPropaneLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 528.8 - 1.4 * T - 3.66e-3 * T**2
        specificHeat = (2.505 + 7.59e-3 * T + 5.71e-5 * T**2 + 4.98e-7 * T**3) * 1000
        dynamicViscosity = (125.6 - 1.31 * T + 7.9e-3 * T**2 - 5e-5 * T**3) * 1e-6
        conductivity = 0.1061 - 5.19e-4 * T + 9.26e-7 * T**2
        surfaceTension = (10.265 - 0.129 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# Propane (saturated vapor)
def getPropaneVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 10.264 + 0.304 * T + 3.9e-3 * T**2 + 2.61e-5 * T**3
        specificHeat = (1.781 + 9.42e-3 * T + 7.48e-5 * T**2 + 7.3e-7 * T**3) * 1000
        dynamicViscosity = (7.441 + 0.0317 * T + 1.21e-4 * T**2) * 1e-6
        conductivity = (15.719 + 0.122 * T + 5.68e-4 * T**2) * 1e-3
        latentHeat = (374.8 - 1.47 * T - 6.17e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# CO2 (saturated liquid)
def getCO2LProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 922.8 - 6.29 * T - 0.0353 * T**2
        specificHeat = (2.527 + 0.0424 * T + 1.49e-3 * T**2 + 1.78e-5 * T**3) * 1000
        dynamicViscosity = (99.5 - 1.76 * T + 8.14e-3 * T**2 - 1.72e-4 * T**3) * 1e-6
        conductivity = 0.1102 - 1.22e-3 * T + 2.44e-7 * T**2
        surfaceTension = (4.578 - 0.186 * T + 6.84e-4 * T**2) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# CO2 (saturated vapor)
def getCO2VProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 97.595 + 3.32 * T + 0.0594 * T**2 + 5.1e-4 * T**3
        specificHeat = (1.797 + 0.0484 * T + 2.46e-3 * T**2 + 7.49e-5 * T**3 + 7.73e-7 * T**4) * 1000
        dynamicViscosity = (14.978 + 0.119 * T + 1.01e-3 * T**2) * 1e-6
        conductivity = (19.62 + 0.406 * T + 0.0109 * T**2 + 1.23e-4 * T**3) * 1e-3
        latentHeat = (228.5 - 3.18 * T - 0.0202 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# Ammonia (saturated liquid)
def getAmmoniaLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 638.6 - 1.38 * T - 2.42e-3 * T**2
        specificHeat = (4.615 + 5.52e-3 * T + 3.75e-5 * T**2 + 6.05e-7 * T**3) * 1000
        dynamicViscosity = (169.2 - 1.83 * T + 0.0183 * T**2 - 1.67e-4 * T**3) * 1e-6
        conductivity = 0.559 - 3.06e-3 * T + 4e-6 * T**2
        surfaceTension = (33.408 - 0.337 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# Ammonia (saturated vapor)
def getAmmoniaVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 3.423 + 0.122 * T + 1.84e-3 * T**2 + 1.27e-5 * T**3
        specificHeat = (2.677 + 0.0148 * T + 1.27e-4 * T**2 + 6.37e-7 * T**3) * 1000
        dynamicViscosity = (9.053 + 0.0309 * T + 2.61e-5 * T**2) * 1e-6
        conductivity = (23.353 + 0.0969 * T + 7.3e-4 * T**2) * 1e-3
        latentHeat = (1262.4 - 3.62 * T - 0.0116 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-12 (saturated liquid)
def getR12LProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1396.2 - 3.28 * T - 6.84e-3 * T**2
        specificHeat = (0.9335 + 1.84e-3 * T + 1.27e-5 * T**2 + 1.04e-7 * T**3) * 1000
        dynamicViscosity = (244.6 - 2.6 * T + 0.0188 * T**2 - 1.46e-4 * T**3) * 1e-6
        conductivity = 0.0758 - 3.59e-4 * T + 3.27e-7 * T**2
        surfaceTension = (11.922 - 0.133 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-12 (saturated vapor)
def getR12VProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 17.735 + 0.556 * T + 7.28e-3 * T**2 + 4.59e-5 * T**3
        specificHeat = (0.6291 + 2.4e-3 * T + 1.57e-5 * T**2 + 1.57e-7 * T**3) * 1000
        dynamicViscosity = (10.611 + 0.0402 * T + 6.12e-5 * T**2) * 1e-6
        conductivity = (8.848 + 0.0567 * T + 1.68e-4 * T**2) * 1e-3
        latentHeat = (152.8 - 0.508 * T - 1.77e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-22 (saturated liquid)
def getR22LProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1281.8 - 3.48 * T - 8.95e-3 * T**2
        specificHeat = (1.167 + 2.69e-3 * T + 3.12e-5 * T**2 + 2.73e-7 * T**3) * 1000
        dynamicViscosity = (215.5 - 2.35 * T + 0.0158 * T**2 - 1.23e-4 * T**3) * 1e-6
        conductivity = 0.0947 - 4.55e-4 * T + 4.11e-8 * T**2
        surfaceTension = (11.865 - 0.149 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-22 (saturated vapor)
def getR22VProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 20.983 + 0.664 * T + 9.24e-3 * T**2 + 6.53e-5 * T**3
        specificHeat = (0.736 + 4.17e-3 * T + 4.3e-5 * T**2 + 4.32e-7 * T**3) * 1000
        dynamicViscosity = (11.359 + 0.0448 * T + 1.04e-4 * T**2) * 1e-6
        conductivity = (9.386 + 0.0724 * T + 3.79e-4 * T**2) * 1e-3
        latentHeat = (205.1 - 0.834 * T - 3.28e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-134a (saturated liquid)
def getR134aLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1295 - 3.39 * T - 8.12e-3 * T**2
        specificHeat = (1.339 + 2.68e-3 * T + 2.39e-5 * T**2 + 2.36e-7 * T**3) * 1000
        dynamicViscosity = (265.1 - 3.38 * T + 0.0315 * T**2 - 2.81e-4 * T**3) * 1e-6
        conductivity = 0.092 - 4.49e-4 * T + 4.06e-7 * T**2
        surfaceTension = (11.733 - 0.143 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-134a (saturated vapor)
def getR134aVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 14.211 + 0.5 * T + 7.75e-3 * T**2 + 5.8e-5 * T**3
        specificHeat = (0.895 + 4.47e-3 * T + 3.36e-5 * T**2 + 3.1e-7 * T**3) * 1000
        dynamicViscosity = (10.718 + 0.0389 * T + 6.98e-5 * T**2) * 1e-6
        conductivity = (11.496 + 0.0912 * T + 2.08e-4 * T**2) * 1e-3
        latentHeat = (198.6 - 0.787 * T - 2.66e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-404A (saturated liquid)
def getR404ALProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1150.9 - 4.04 * T - 0.0163 * T**2
        specificHeat = (1.378 + 3.98e-3 * T + 8.06e-5 * T**2 + 1.2e-6 * T**3) * 1000
        dynamicViscosity = (177.6 - 2.38 * T + 0.022 * T**2 - 2.08e-4 * T**3) * 1e-6
        conductivity = 0.0739 - 3.9e-4 * T + 5.53e-7 * T**2
        surfaceTension = (7.545 - 0.118 * T) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-404A (saturated vapor)
def getR404AVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 29.597 + 0.95 * T + 0.016 * T**2 + 1.51e-4 * T**3
        specificHeat = (0.983 + 5.7e-3 * T + 1.15e-4 * T**2 + 1.95e-6 * T**3) * 1000
        dynamicViscosity = (12.595 + 0.0681 * T + 4.01e-4 * T**2) * 1e-6
        conductivity = (14.469 + 0.129 * T + 1e-3 * T**2) * 1e-3
        latentHeat = (166.1 - 0.956 * T - 4.99e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-504A (saturated liquid)
def getR504ALProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 1160.3 - 4.77 * T - 0.0245 * T**2
        specificHeat = (1.358 + 3.72e-3 * T + 1.98e-4 * T**2 + 4.01e-6 * T**3) * 1000
        dynamicViscosity = (148.5 - 1.9 * T + 0.0143 * T**2 - 1.53e-4 * T**3) * 1e-6
        conductivity = 0.0947 - 5.69e-4 * T - 2.22e-8 * T**2
        surfaceTension = (7.013 - 0.14 * T + 3e-4 * T**2) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-504A (saturated vapor)
def getR504AVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 38.703 + 1.21 * T + 0.0236 * T**2 + 2.69e-4 * T**3
        specificHeat = (1.017 + 6.15e-3 * T + 3.07e-4 * T**2 + 6.44e-6 * T**3) * 1000
        dynamicViscosity = (12.909 + 0.0792 * T + 6.09e-4 * T**2) * 1e-6
        conductivity = (11.777 + 0.165 * T + 2.58e-3 * T**2) * 1e-3
        latentHeat = (184.1 - 1.26 * T - 8.22e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
    return results


# R-508B (saturated liquid)
def getR508BLProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 997.9 - 8.72 * T - 0.0297 * T**2
        specificHeat = (2.038 + 0.0387 * T + 5.61e-4 * T**2 + 2.78e-6 * T**3) * 1000
        dynamicViscosity = (74.768 - 2.33 * T - 0.0179 * T**2 - 3.02e-4 * T**3) * 1e-6
        conductivity = 0.0528 - 4.63e-4 * T + 6.4e-7 * T**2
        surfaceTension = (0.82 - 0.118 * T + 3.26e-4 * T**2) * 1e-3
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, surfaceTension=surfaceTension)
    return results


# R-508B (saturated vapor)
def getR508BVProperties(temperatures):
    results = {}
    for key, T in temperatures.items():
        density = 212.061 + 6.77 * T + 0.0808 * T**2 + 3.44e-4 * T**3
        specificHeat = (2.16 + 0.0622 * T + 9.3e-4 * T**2 + 4.71e-6 * T**3) * 1000
        dynamicViscosity = (16.801 + 0.135 * T + 5.66e-4 * T**2) * 1e-6
        conductivity = (21.331 + 0.32 * T + 1.79e-3 * T**2) * 1e-3
        latentHeat = (75 - 1.6 * T - 6.43e-3 * T**2) * 1000
        results[key] = FluidProperties(density, specificHeat, dynamicViscosity, conductivity, latentHeat=latentHeat)
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



