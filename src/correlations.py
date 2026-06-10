from dimensionless import calculateRayleigh, calculateGrashof, calculatePrandtl, calculateReynolds
from math import cos, sin, radians, log
from fluids import fluidTemperatureRanges

def validateTemperatureRange(fluid, temperatures, fluidKeys, fluidPairKeys=None, fluidPair=None):
    minT, maxT = fluidTemperatureRanges[fluid]
    for key in fluidKeys:
        value = temperatures[key]
        if not (minT <= value <= maxT):
            return (None, f"Temperature '{key}' = {value}°C is outside the valid range [{minT}, {maxT}]°C for {fluid}")

    if fluidPair is not None:
        minT, maxT = fluidTemperatureRanges[fluidPair]
        for key in fluidPairKeys:
            value = temperatures[key]
            if not (minT <= value <= maxT):
                return (None, f"Temperature '{key}' = {value}°C is outside the valid range [{minT}, {maxT}]°C for {fluidPair}")

    return (True, None)


def internalNaturalConvectionNarrowVerticalDuct(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    length = d["characteristic length"]["length"]
    characteristicLength = d["characteristic length"]["result"]
    coefficient = d["coefficient"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if rayleigh < length / characteristicLength:
        return (coefficient * rayleigh, None)
    else:
        return (None, "Non suitable inputs for this correlation")
    


def internalNaturalConvectionVerticalRectangularCavity(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["mean"])
    if not isValid:
        return (None, message)

    length = d["characteristic length"]["length"]
    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["mean"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)
    
    if rayleigh < 1000:
        return (1, None)
    else:
        ratio = length / characteristicLength
        if 1 < ratio < 2:
            if not 1e3 < prandtl / (0.2 + prandtl) * rayleigh:
                return (None, "Outside the recommended operating range")
            return (0.18 * (prandtl * rayleigh / (0.2 + prandtl))**0.29, None)

        elif 2 <= ratio < 20:
            if not rayleigh < 1e10:
                return (None, "Outside the recommended operating range")
            return (0.22 * (prandtl * rayleigh / (0.2 + prandtl))**0.28 * ratio**(-1/4), None)
            
        elif 20 <= ratio < 40:
            if not 1e4 < rayleigh < 1e7 or not 1 < prandtl < 2e4:
                return (None, "Outside the recommended operating range")
            return (0.42 * rayleigh**(1/4) * prandtl**0.012 * ratio**(-0.3), None)
        else:
            return (None, "Non suitable inputs for this correlation")



def internalNaturalConvectionInclinedRectangularCavity(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["mean"])
    if not isValid:
        return (None, message)

    length = d["characteristic length"]["length"]
    characteristicLength = d["characteristic length"]["result"]
    angle = d["angle"]
    props = fluidProperties["mean"]

    if angle == 90:
        return (None, "Use vertical rectangular cavity correlation for 90°")

    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)
    criticalRayleigh = 1708 / cos(radians(angle))

    def getCriticalAngle():
        criticalAngleDict = {"1": 25, "3": 53, "6": 60, "12": 67, ">12": 70}
        quotient = length / characteristicLength
        def getClosestValue(value):
            if value > 12:
                return ">12"
            options = [1, 3, 6, 12]
            return min(options, key=lambda x: abs(value - x))
        aproxQuotient = str(getClosestValue(quotient))
        return criticalAngleDict[aproxQuotient]
    
    criticalAngle = getCriticalAngle()

    if rayleigh < criticalRayleigh:
        return (1, None)
    
    elif rayleigh >= criticalRayleigh and angle <= criticalAngle:
        x = (rayleigh * cos(radians(angle)) / 5830)**(1/3) - 1
        if x < 0:
            x = 0
        return (1 + 1.44 * (1 - 1708 / rayleigh / cos(radians(angle))) * (1 - 1708 * (sin(1.8 * radians(angle)))**1.6 / rayleigh / cos(radians(angle))) + x, None)
    
    elif rayleigh >= criticalRayleigh and angle > criticalAngle:
        if criticalAngle < angle < 90:
            result, message = internalNaturalConvectionVerticalRectangularCavity(d, fluidProperties)
            if result is None:
                return (None, message)
            return (result * (sin(radians(angle)))**(1/4), None)
        
        elif 90 < angle < 180:
            result, message = internalNaturalConvectionVerticalRectangularCavity(d, fluidProperties)
            if result is None:
                return (None, message)
            return (1 + (result - 1) * sin(radians(angle)), None)
            
        else:
            return (None, "Non suitable inputs for this correlation")



def internalNaturalConvectionHorizontalRectangularCavity(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["mean"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    topSurface = d["top surface"]
    props = fluidProperties["mean"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    def calculateForHotterLowerSurface():
        if rayleigh < 1708:
            return (1, None)
        else:
            return internalNaturalConvectionInclinedRectangularCavity(d, fluidProperties)


    if temperatures["surface 1"] > temperatures["surface 2"] and topSurface == 1:
        return (1, None)
    
    elif temperatures["surface 1"] < temperatures["surface 2"] and topSurface == 1:
        return calculateForHotterLowerSurface()

    elif temperatures["surface 1"] > temperatures["surface 2"] and topSurface == 2:
        return calculateForHotterLowerSurface()

    elif temperatures["surface 1"] < temperatures["surface 2"] and topSurface == 2:
        return (1, None)

    else:
        return (None, "Invalid case")
    


def internalNaturalConvectionSphericalCavity(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if 1e4 <= rayleigh < 1e9:
        C = 0.59
        n = 1/4
    elif 1e9 <= rayleigh <= 1e12:
        C = 0.13
        n = 1/3   
    else:
        return (None, "Outside the recommended operating range")

    return (C * rayleigh**n, None)



def internalNaturalConvectionConcentricCylinders(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["mean"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    innerDiameter = d["characteristic length"]["inner diameter"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    props = fluidProperties["mean"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if not (0.7 <= prandtl <= 6000) or not (10 <= log(outerDiameter/innerDiameter)**4 / characteristicLength**3 / (1 / innerDiameter**(3/5) + 1 / outerDiameter**(3/5))**5 * rayleigh <= 1e7):
        return (None, "Outside the recommended operating range")

    return (props.conductivity * 0.386 * log(outerDiameter/innerDiameter) / characteristicLength**(3/4) / (1 / innerDiameter**(3/5) + 1 / outerDiameter**(3/5))**(5/4) * (prandtl / (0.861 + prandtl))**(1/4) * rayleigh**(1/4), None)

    

def internalNaturalConvectionConcentricSpheres(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["mean"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    innerDiameter = d["characteristic length"]["inner diameter"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    props = fluidProperties["mean"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if not (0.7 <= prandtl <= 4200) or not (10 <= characteristicLength / (outerDiameter * innerDiameter)**4 / (innerDiameter**(-7/5) + outerDiameter**(-7/5))**5 * rayleigh <= 1e7):
        return (None, "Outside the recommended operating range")

    return (props.conductivity * 0.74 * characteristicLength**(1/4) / (outerDiameter * innerDiameter) / (innerDiameter**(-7/5) + outerDiameter**(-7/5))**(5/4) * (prandtl / (0.861 + prandtl))**(1/4) * rayleigh**(1/4), None)



def externalNaturalConvectionVerticalFlatPlate(d, fluidProperties, g=9.81):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density, g=g)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if rayleigh < 1e9:
        return (0.68 + 0.67 * rayleigh**(1/4) / (1 + (0.492 / prandtl)**(9/16))**(4/9), None)
    else:
        return ((0.825 + 0.387 * rayleigh**(1/6) / (1 + (0.492 / prandtl)**(9/16))**(8/27))**2, None)



def externalNaturalConvectionInclinedFlatPlate(d, fluidProperties):
    angle = d["angle"]

    return externalNaturalConvectionVerticalFlatPlate(d, fluidProperties, g=9.81*cos(radians(angle)))



def externalNaturalConvectionHorizontalFlatPlateTopHot(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if 1e4 <= rayleigh <= 1e7:
        return (0.54 * rayleigh**(1/4), None)
    
    elif 1e7 < rayleigh <= 1e11:
        return (0.15 * rayleigh**(1/3), None)

    else:
        return (None, "Outside the recommended operating range")



def externalNaturalConvectionHorizontalFlatPlateTopCold(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if not (1e5 <= rayleigh <= 1e11):
        return (None, "Outside the recommended operating range")
    
    return (0.27 * rayleigh**(1/4), None)



def externalNaturalConvectionVerticalCylinder(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    diameter = d["characteristic length"]["diameter"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)

    if not (diameter / characteristicLength >= 35 / grashof**(1/4)):
        return (None, "Non suitable inputs for this correlation")

    return externalNaturalConvectionVerticalFlatPlate(d, fluidProperties)


def externalNaturalConvectionInclinedCylinder(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    diameter = d["characteristic length"]["diameter"]
    angle = d["angle"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)

    if not (diameter / characteristicLength >= 35 / grashof**(1/4)):
        return (None, "Non suitable inputs for this correlation")
    
    return externalNaturalConvectionVerticalFlatPlate(d, fluidProperties, g=9.81*cos(radians(angle)))


def externalNaturalConvectionHorizontalCylinder(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if rayleigh < 1e9:
        return (0.36 + 0.518 * rayleigh**(1/4) / (1 + (0.559 / prandtl)**(9/16))**(4/9), None)

    else:
        return ((0.6 + 0.387 * (rayleigh / (1 + (0.559 / prandtl)**(9/16))**(16/9))**(1/6))**2, None)

  

def externalNaturalConvectionSphere(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)

    characteristicLength = d["characteristic length"]["result"]
    props = fluidProperties["film"]
    grashof = calculateGrashof(temperatures, characteristicLength, props.dynamicViscosity, props.density)
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    rayleigh = calculateRayleigh(grashof, prandtl)

    if not (prandtl >= 0.7) or not (rayleigh <= 1e11):
        return (None, "Outside the recommended operating range")
    
    return (2 + 0.589 * rayleigh**(1/4) / (1 + (0.469 / prandtl)**(9/16))**(4/9), None)



def internalForcedConvectionCircularDuct(d, fluidProperties):
    temperatures = d["temperatures"]

    if "surface" in temperatures:
        isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid", "surface"])
        if not isValid:
            return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)

    def calculateFrictionFactor(re):
        return 1 / (0.79 * log(re) - 1.64)**2
    
    if reynolds < 2300:
        length = d["characteristic length"]["length"]
        if not (100 < reynolds * prandtl * characteristicLength / length < 1500) or not (prandtl > 0.7):
            return (None, "Outside the recommended operating range")
        
        propsSurface = fluidProperties["surface"]
        return (3.66 + 0.0668 * characteristicLength / length * reynolds * prandtl / (1 + 0.045 * (characteristicLength / length * reynolds * prandtl)**(2/3)) * (propsFluid.dynamicViscosity / propsSurface.dynamicViscosity)**0.14, None)

    elif 2300 <= reynolds < 1e4:
        if not (0.5 < prandtl < 2000):
            return (None, "Outside the recommended operating range")

        frictionFactor = calculateFrictionFactor(reynolds)
        return ((frictionFactor / 8 * (reynolds - 1000) * prandtl) / (1 + 12.7 * (frictionFactor / 8)**(1/2) * (prandtl**(2/3) - 1)), None)
    
    elif 1e4 <= reynolds < 5e6:
        if not (0.5 < prandtl < 2000):
            return (None, "Outside the recommended operating range")
        
        frictionFactor = calculateFrictionFactor(reynolds)
        return ((frictionFactor / 8 * reynolds * prandtl) / (1.07 + 12.7 * (frictionFactor / 8)**(1/2) * (prandtl**(2/3) - 1)), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def internalForcedConvectionTriangularDuctConstantT(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        return (2.47, None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)

   

def internalForcedConvectionTriangularDuctConstantQ(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        return (3.11, None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionSquaredDuctConstantT(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        return (2.98, None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionSquaredDuctConstantQ(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        return (3.61, None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionRectangularDuctConstantT(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    ratio = d["characteristic length"]["ratio"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        def getNusseltFromRatio():
            ratioDict = {"1.43": 3.08, "2": 3.39, "3": 3.96, "4": 4.44, "8": 5.6, ">8": 7.54}
            def getClosestValue(value):
                if value > 8:
                    return ">8"
                options = [1.43, 2, 3, 4, 8]
                return min(options, key=lambda x: abs(value - x))
            aproxRatio = str(getClosestValue(ratio))
            return ratioDict[aproxRatio]
        
        return (getNusseltFromRatio(), None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionRectangularDuctConstantQ(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    ratio = d["characteristic length"]["ratio"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    
    if reynolds < 2300:
        def getNusseltFromRatio():
            ratioDict = {"1.43": 3.73, "2": 4.12, "3": 4.79, "4": 5.33, "8": 6.49, ">8": 8.23}
            def getClosestValue(value):
                if value > 8:
                    return ">8"
                options = [1.43, 2, 3, 4, 8]
                return min(options, key=lambda x: abs(value - x))
            aproxRatio = str(getClosestValue(ratio))
            return ratioDict[aproxRatio]
        
        return (getNusseltFromRatio(), None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionBetweenParallelPlanes(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    length = d["characteristic length"]["length"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    
    if reynolds < 2800:        
        return (7.54 + 0.03 * characteristicLength / length * reynolds * prandtl / (1 + 0.016 * (characteristicLength / length * reynolds * prandtl)**(2/3)), None)

    else:
        return internalForcedConvectionCircularDuct(d, fluidProperties)



def internalForcedConvectionAnnularDuctInnerHeatFlow(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    length = d["characteristic length"]["length"]
    innerDiameter = d["characteristic length"]["inner diameter"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    
    if reynolds < 2300:
        if not (0.1 < prandtl < 1000):
            return (None, "Outside the recommended operating range")
                
        return (3.66 + 1.2 * (innerDiameter / outerDiameter)**(-0.8) + (1 + 0.14 * (innerDiameter / outerDiameter)**(-0.5)) * 0.19 * (reynolds * prandtl * characteristicLength / length)**0.8 / (1 + 0.117 * (reynolds * prandtl * characteristicLength / length)**0.467), None)

    else:
        result, message = internalForcedConvectionCircularDuct(d, fluidProperties)
        if result is None:
            return (None, message)
        return (result * 0.86 * (innerDiameter / outerDiameter)**(-0.16), None)



def internalForcedConvectionAnnularDuctOuterHeatFlow(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    length = d["characteristic length"]["length"]
    innerDiameter = d["characteristic length"]["inner diameter"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    
    if reynolds < 2300:
        if not (0.1 < prandtl < 1000):
            return (None, "Outside the recommended operating range")
                
        return (3.66 + 1.2 * (innerDiameter / outerDiameter)**(0.5) + (1 + 0.14 * (innerDiameter / outerDiameter)**(1/3)) * 0.19 * (reynolds * prandtl * characteristicLength / length)**0.8 / (1 + 0.117 * (reynolds * prandtl * characteristicLength / length)**0.467), None)

    else:
        result, message = internalForcedConvectionCircularDuct(d, fluidProperties)
        if result is None:
            return (None, message)
        return (result * (1 - 0.14 * (innerDiameter / outerDiameter)**(0.6)), None)



def internalForcedConvectionAnnularDuctInnerOuterHeatFlow(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    length = d["characteristic length"]["length"]
    innerDiameter = d["characteristic length"]["inner diameter"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    
    if reynolds < 2300:
        if not (0.1 < prandtl < 1000):
            return (None, "Outside the recommended operating range")
                
        return (3.66 + (4 - 0.012 / (innerDiameter / outerDiameter + 0.2)) * (innerDiameter / outerDiameter)**0.04 + (1 + 0.14 * (innerDiameter / outerDiameter)**0.1) * 0.19 * (reynolds * prandtl * characteristicLength / length)**0.8 / (1 + 0.117 * (reynolds * prandtl * characteristicLength / length)**0.467), None)

    else:
        result, message = internalForcedConvectionCircularDuct(d, fluidProperties)
        if result is None:
            return (None, message)
        return (result * (0.86 * (innerDiameter / outerDiameter)**0.84 + 1 - 0.14 * (innerDiameter / outerDiameter)**0.6) / (1 + innerDiameter / outerDiameter), None)

    


def internalForcedConvectionHelicalCoil(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["fluid", "surface"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    coilDiameter = d["characteristic length"]["coil diameter"]
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    propsSurface = fluidProperties["surface"]
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    prandtlSurface = calculatePrandtl(propsSurface.dynamicViscosity, propsSurface.specificHeat, propsSurface.conductivity)
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)

    ratio = characteristicLength / coilDiameter
    criticalReynolds = 2300 * (1 + 8.6 * ratio**0.45)

    def nusseltLaminar(re):
        n = 0.5 + 0.2903 * ratio**0.194
        return 3.65 + 0.08 * (1 + 0.8 * ratio**0.9) * re**n * prandtl**(1/3) * (prandtl / prandtlSurface)**0.14

    def nusseltTurbulent(re):
        frictionFactor = (0.3164 / re**0.25 + 0.03 * ratio**0.5) * (propsSurface.dynamicViscosity / propsFluid.dynamicViscosity)**0.27
        return (frictionFactor / 8 * re * prandtl) / (1.07 + 12.7 * (frictionFactor / 8)**(1/2) * (prandtl**(2/3) - 1))

    if reynolds < criticalReynolds:
        return (nusseltLaminar(reynolds), None)
    
    elif criticalReynolds <= reynolds <= 22000:
        C = (22000 - reynolds) / (22000 - criticalReynolds)
        return (C * nusseltLaminar(criticalReynolds) + (1 - C) * nusseltTurbulent(22000), None)
    
    else:
        return (nusseltTurbulent(reynolds), None)



def externalForcedConvectionFlatPlate(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    if reynolds < 5e5:
        if prandtl <= 0.5:
            return (1.128 * (reynolds * prandtl)**(1/2), None)
        else:
            return (0.664 * reynolds**(1/2) * prandtl**(1/3), None)
    else:
        if not (0.6 < prandtl < 60) or not (5e5 < reynolds < 1e8):
            return (None, "Outside the recommended operating range")

        return ((0.037 * reynolds**(4/5) - 871) * prandtl**(1/3), None)



def externalForcedConvectionPerpendicularFlowCylinders(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    prandtl = calculatePrandtl(props.dynamicViscosity, props.specificHeat, props.conductivity)
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    if reynolds * prandtl < 0.2:
        return (1 / (0.8237 - log((reynolds * prandtl)**(1/2))), None)
    
    else:
        if 2e4 <= reynolds < 4e5:
            return (0.3 + 0.62 * reynolds**(1/2) * prandtl**(1/3) / (1 + (0.4 / prandtl)**(2/3))**(1/4) * (1 + (reynolds / 282000)**(1/2)), None)
        
        elif (1e2 <= reynolds < 2e4) or (4e5 <= reynolds < 1e7):
            return (0.3 + 0.62 * reynolds**(1/2) * prandtl**(1/3) / (1 + (0.4 / prandtl)**(2/3))**(1/4) * (1 + (reynolds / 282000)**(5/8))**(4/5), None)
        
        else:
            return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowSquareFaceOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 2500 <= reynolds < 5000:
        return (calculateNusselt(reynolds, 0.16, 0.699), None)
    
    elif 5000 <= reynolds < 1e5:
        return (calculateNusselt(reynolds, 0.092, 0.675), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowSquareAristOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 2500 <= reynolds < 5000:
        return (calculateNusselt(reynolds, 0.224, 0.612), None)
    
    elif 5000 <= reynolds < 1e5:
        return (calculateNusselt(reynolds, 0.222, 0.588), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowHexagonFaceOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 2500 <= reynolds < 19500:
        return (calculateNusselt(reynolds, 0.144, 0.638), None)
    
    elif 19500 <= reynolds < 1e5:
        return (calculateNusselt(reynolds, 0.035, 0.782), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowHexagonAristOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 5000 <= reynolds <= 1e5:
        return (calculateNusselt(reynolds, 0.138, 0.638), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowRectangleFaceOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 4000 <= reynolds <= 15000:
        return (calculateNusselt(reynolds, 0.205, 0.731), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowEllipseWideOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 3000 <= reynolds <= 15000:
        return (calculateNusselt(reynolds, 0.085, 0.804), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionPerpendicularFlowEllipseNarrowOriented(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    props = fluidProperties["film"]
    reynolds = calculateReynolds(props.density, fluidVelocity, characteristicLength, props.dynamicViscosity)

    def calculateNusselt(re, C, n):
        return C * re**n

    if 2500 <= reynolds <= 15000:
        return (calculateNusselt(reynolds, 0.224, 0.612), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionSphere(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film", "surface"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    fluidVelocity = d["fluid velocity"]
    propsFluid = fluidProperties["fluid"]
    propsSurface = fluidProperties["surface"]
    reynolds = calculateReynolds(propsFluid.density, fluidVelocity, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)

    if not (0.71 < prandtl < 380) or not (3.5 < reynolds < 7.6e4) or not (1 < propsFluid.dynamicViscosity / propsSurface.dynamicViscosity < 3.2):
        return (None, "Outside the recommended operating range")
    
    return (2 + (0.4 * reynolds**(1/2) + 0.06 * reynolds**(2/3)) * prandtl**0.4 * (propsFluid.dynamicViscosity / propsSurface.dynamicViscosity)**(1/4), None)



def externalForcedConvectionCrossFlowTubeBundleSquare(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film", "surface"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    x1 = d["characteristic length"]["x1"]  
    inletVelocity = d["fluid velocity"]["inlet velocity"]
    nCols = d["number of columns"]
    propsFluid = fluidProperties["fluid"]
    propsSurface = fluidProperties["surface"]
    vMax = inletVelocity * x1 / (x1 - characteristicLength)
    reynoldsMax = calculateReynolds(propsFluid.density, vMax, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    prandtlSurface = calculatePrandtl(propsSurface.dynamicViscosity, propsSurface.specificHeat, propsSurface.conductivity)

    def calculateNusselt(reMax, pr, prSup, c1, c2, n):
        return c1 * c2 * reMax**n * pr**0.36 * (pr / prSup)**(1/4)
    
    def getC2(columns):
        c2Dict = {
            1: 0.7, 2: 0.8, 3: 0.86, 4: 0.9, 5: 0.92,
            7: 0.95, 10: 0.97, 13: 0.98, 16: 0.99, 20: 1.0
        }

        if columns >= 20:
            return 1.0
        if columns in c2Dict:
            return c2Dict[columns]

        # Interpolación lineal
        keys = sorted(c2Dict.keys())
        for i in range(len(keys) - 1):
            if keys[i] < columns < keys[i + 1]:
                x0, x1 = keys[i], keys[i + 1]
                y0, y1 = c2Dict[x0], c2Dict[x1]
                return y0 + (y1 - y0) * (columns - x0) / (x1 - x0)

    c2 = getC2(nCols)

    if 10 <= reynoldsMax < 100:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.8, c2, 0.4), None)
    
    elif 100 <= reynoldsMax < 1000:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.51, c2, 0.5), None)
    
    elif 1000 <= reynoldsMax < 2e5:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.27, c2, 0.63), None)
    
    elif 2e5 <= reynoldsMax < 2e6:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.021, c2, 0.84), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def externalForcedConvectionCrossFlowTubeBundleTriangular(d, fluidProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film", "surface"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]  
    x1 = d["characteristic length"]["x1"]
    x2 = d["characteristic length"]["x2"]
    x3 = d["characteristic length"]["x3"] 
    inletVelocity = d["fluid velocity"]["inlet velocity"]
    nCols = d["number of columns"]
    propsFluid = fluidProperties["fluid"]
    propsSurface = fluidProperties["surface"]

    def getVMax():
        if 2 * (x3 - characteristicLength) >= x1 - characteristicLength:
            return inletVelocity * x1 / (x1 - characteristicLength)
        else:
            return inletVelocity * x1 / 2 / (x3 - characteristicLength)
        
    vMax = getVMax()
    reynoldsMax = calculateReynolds(propsFluid.density, vMax, characteristicLength, propsFluid.dynamicViscosity)
    prandtl = calculatePrandtl(propsFluid.dynamicViscosity, propsFluid.specificHeat, propsFluid.conductivity)
    prandtlSurface = calculatePrandtl(propsSurface.dynamicViscosity, propsSurface.specificHeat, propsSurface.conductivity)

    def calculateNusselt(reMax, pr, prSup, c1, c2, n):
        return c1 * c2 * reMax**n * pr**0.36 * (pr / prSup)**(1/4)
    
    def getC2(columns):
        c2Dict = {
            1: 0.64, 2: 0.76, 3: 0.84, 4: 0.89, 5: 0.92,
            7: 0.95, 10: 0.97, 13: 0.98, 16: 0.99, 20: 1.0
        }
        
        if columns >= 20:
            return 1.0
        if columns in c2Dict:
            return c2Dict[columns]

        # Interpolación lineal
        keys = sorted(c2Dict.keys())
        for i in range(len(keys) - 1):
            if keys[i] < columns < keys[i + 1]:
                x0, x1 = keys[i], keys[i + 1]  
                y0, y1 = c2Dict[x0], c2Dict[x1]
                return y0 + (y1 - y0) * (columns - x0) / (x1 - x0)

    c2 = getC2(nCols)

    if 10 <= reynoldsMax < 100:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.9, c2, 0.4), None)
    
    elif 100 <= reynoldsMax < 1000:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.51, c2, 0.5), None)
    
    elif 1000 <= reynoldsMax < 2e5:
        if x1 / x2 < 2:
            c1 = 0.35 * (x1 / x2)**0.2
            return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, c1, c2, 0.6), None)
        
        else:
            return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.4, c2, 0.6), None)
        
    elif 2e5 <= reynoldsMax < 2e6:
        return (calculateNusselt(reynoldsMax, prandtl, prandtlSurface, 0.022, c2, 0.84), None)
    
    else:
        return (None, "Non suitable inputs for this correlation")



def naturalCondensationVerticalFlatSurface(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81

    return (0.943 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * propsLiquidFilm.conductivity**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / characteristicLength)**(1/4), None)
    


def naturalCondensationInclinedFlatSurface(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    angle = d["angle"]

    result, message = naturalCondensationVerticalFlatSurface(d, liquidProperties, vaporProperties)
    
    if result is None:
        return (None, message)
    
    return (result * sin(radians(angle))**(1/4), None)
    


def naturalCondensationHorizontalFlatSurfaceStrip(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81

    return (1.079 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * characteristicLength**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / propsLiquidFilm.conductivity)**(1/5), None)
    


def naturalCondensationHorizontalFlatSurfaceDisk(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81

    return (1.368 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * characteristicLength**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / propsLiquidFilm.conductivity)**(1/5), None)
    


def naturalCondensationHorizontalFlatSurfaceOtherStrip(d, liquidProperties, vaporProperties):
    return naturalCondensationHorizontalFlatSurfaceStrip(d, liquidProperties, vaporProperties)
    


def naturalCondensationHorizontalFlatSurfaceOtherDisk(d, liquidProperties, vaporProperties):
    return naturalCondensationHorizontalFlatSurfaceDisk(d, liquidProperties, vaporProperties)



def naturalCondensationVerticalCylinder(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    diameter = d["characteristic length"]["diameter"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81
    filmThickness = (4 * characteristicLength * propsLiquidFilm.dynamicViscosity * propsLiquidFilm.conductivity * (saturationTemperature - surfaceTemperature) / (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat))**(1/4)
    
    if filmThickness < 0.1 * diameter / 2:
       return naturalCondensationVerticalFlatSurface(d, liquidProperties, vaporProperties)
    
    else:
        return (None, "Non suitable inputs for this correlation")
    


def naturalCondensationHorizontalCylinder(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81

    return (0.725 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * propsLiquidFilm.conductivity**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / characteristicLength)**(1/4), None)
    


def naturalCondensationHorizontalTubeBundle(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    nRows = d["number of rows"]

    result, message = naturalCondensationHorizontalCylinder(d, liquidProperties, vaporProperties)
    
    if result is None:
        return (None, message)
    
    return (result * nRows**(-2/9), None)
    


def naturalCondensationInclinedCylinder(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    angle = d["angle"]

    result, message = naturalCondensationHorizontalCylinder(d, liquidProperties, vaporProperties)
    
    if result is None:
        return (None, message)
    return (result * (cos(radians(angle)))**(1/4), None)
    


def naturalCondensationSphere(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    g = 9.81

    return (0.815 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * propsLiquidFilm.conductivity**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / characteristicLength)**(1/4), None)
    


def internalForcedCondensationCircularDuct(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"], ["saturation"], d["fluid pair"])
    if not isValid:
        return (None, message)
    
    saturationTemperature = d["temperatures"]["saturation"]
    surfaceTemperature = d["temperatures"]["surface"]
    characteristicLength = d["characteristic length"]["result"]
    inletVaporVelocity = d["inlet vapor velocity"]
    propsLiquidFilm = liquidProperties["film"]
    propsVaporSaturation = vaporProperties["saturation"]
    propsLiquidSaturation = liquidProperties["saturation"]
    inletVaporReynolds = calculateReynolds(propsVaporSaturation.density, inletVaporVelocity, characteristicLength, propsVaporSaturation.dynamicViscosity)

    if inletVaporReynolds < 35000:
        if saturationTemperature <= surfaceTemperature:
            return (None, "Surface temperature must be lower than saturation temperature for condensation")
        
        g = 9.81
        return (0.555 * (g * propsLiquidFilm.density * (propsLiquidFilm.density - propsVaporSaturation.density) * propsVaporSaturation.latentHeat * propsLiquidFilm.conductivity**3 / propsLiquidFilm.dynamicViscosity / (saturationTemperature - surfaceTemperature) / characteristicLength)**(1/4), None)
    
    else:
        inletVaporQuality = d["vapor quality"]["inlet"]
        outletVaporQuality = d["vapor quality"]["outlet"]

        if not (0 < inletVaporQuality <= 1):
            return (None, "Inlet vapor quality must be between 0 and 1")

        if not (0 <= outletVaporQuality <= 1):
            return (None, "Outlet vapor quality must be between 0 and 1")

        if outletVaporQuality > inletVaporQuality:
            return (None, "For condensation, outlet vapor quality should be lower than inlet vapor quality")
        
        equivalentLiquidVelocity = propsVaporSaturation.density / propsLiquidSaturation.density * inletVaporVelocity / inletVaporQuality
        liquidReynolds = calculateReynolds(propsLiquidSaturation.density, equivalentLiquidVelocity, characteristicLength, propsLiquidSaturation.dynamicViscosity)
        liquidPrandtl = calculatePrandtl(propsLiquidSaturation.dynamicViscosity, propsLiquidSaturation.specificHeat, propsLiquidSaturation.conductivity)
        frictionFactor = 1 / (0.79 *log(liquidReynolds) - 1.64)**2
        nusselt = (frictionFactor / 8 * liquidReynolds * liquidPrandtl) / (1.07 + 12.7 * (frictionFactor / 8)**(1/2) * (liquidPrandtl**(2/3) - 1))
        hl = nusselt * propsLiquidSaturation.conductivity / characteristicLength

        return (hl / 2 * ((1 + inletVaporQuality * (propsLiquidSaturation.density / propsVaporSaturation.density - 1))**(1/2) + (1 + outletVaporQuality * (propsLiquidSaturation.density / propsVaporSaturation.density - 1))**(1/2)), None)
        


def externalForcedCondensationHorizontalCircularDuct(d, liquidProperties, vaporProperties):
    temperatures = d["temperatures"]

    isValid, message = validateTemperatureRange(d["fluid"], temperatures, ["film"])
    if not isValid:
        return (None, message)
    
    characteristicLength = d["characteristic length"]["result"]
    vaporVelocity = d["vapor velocity"]
    propsLiquidFilm = liquidProperties["film"]
    ratio = propsLiquidFilm.density * vaporVelocity * characteristicLength / propsLiquidFilm.dynamicViscosity
    
    if ratio < 1e6:
        hs = 0.9 * ratio**0.5 * propsLiquidFilm.conductivity / characteristicLength

    else:
        hs = 0.59 * ratio**0.5 * propsLiquidFilm.conductivity / characteristicLength
    
    result, message = naturalCondensationHorizontalCylinder(d, liquidProperties, vaporProperties)
    
    if result is None:
        return (None, message)
    
    return ((1 / 2 * hs**2 + (1 / 4 * hs**4 + result**4)**(1/2))**(1/2), None)
