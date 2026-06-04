from dimensionless import calculateRayleigh, calculatePrandtl, calculateReynolds



def internalNaturalConvectionVerticalRectangularCavity(d, fluidProperties):
    isValidCorrelation = None
    temperatures = d["temperatures"]
    characteristicLength = d["characteristic length"]["result"]
    
    props = fluidProperties["mean"]

    rayleigh = calculateRayleigh(temperatures, characteristicLength, props.dynamicViscosity, props.density, props.specificHeat, props.conductivity)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)

      
    length = d["characteristic length"]["length"]
    width = d["characteristic length"]["width"]

    if rayleigh < 1000:
        nusselt = 1
    else:
        ratio = length / width
        if 1 < ratio < 2:
            def isValidCorrelation(rayleigh, prandtl=None):
                if 1e3 < prandtl / (0.2 + prandtl) * rayleigh:
                    return True
                return False
            nusselt = 0.18 * (prandtl * rayleigh / (0.2 + prandtl))**0.29
        elif 2 <= ratio < 20:
            def isValidCorrelation(rayleigh, prandtl=None):
                if rayleigh < 1e10:
                    return True
                return False
            nusselt = 0.22 * (prandtl * rayleigh / (0.2 + prandtl))**0.28 * ratio**(-1/4)
        elif 20 <= ratio < 40:
            def isValidCorrelation(rayleigh, prandtl=None):
                if 1e4 < rayleigh < 1e7 and 1 < prandtl < 2e4:
                    return True
                return False
            nusselt = 0.42 * rayleigh**(1/4) * prandtl**0.012 * ratio**(-0.3)
        else:
            print("Warning: non suitable inputs for this correlation")
            nusselt = None

    if isValidCorrelation and not isValidCorrelation(rayleigh, prandtl):
        print("Warning: non suitable inputs for this correlation")

    return nusselt