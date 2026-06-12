from inputs import menu, fluids, parameters, getInputs1, getInputs2
from fluids import getFluidProperties
from selector import getCorrelation
from results import showInputs, showResults, showValidation

# 1. User selects problem and fluid
inputs1Dict = getInputs1(menu, fluids)

# 2. Get parameters for selected problem
keyTupleInputs = (inputs1Dict["flow type"], inputs1Dict["domain type"], inputs1Dict["geometry1 type"], inputs1Dict["geometry2 type"], inputs1Dict["subtype"])
data2Dict = parameters[keyTupleInputs]

# 3. User enters problem data
inputs2Dict = getInputs2(data2Dict)

# 4. Add fluid info to inputs2Dict
inputs2Dict["fluid"] = inputs1Dict["fluid"]
inputs2Dict["fluid pair"] = inputs1Dict["fluid pair"]
fluid = inputs1Dict["fluid"]
temperatures = inputs2Dict["temperatures"]

# 6. Get correlation and execute
correlation = getCorrelation(keyTupleInputs)

if inputs1Dict["fluid pair"] is not None:
    fluidPair = inputs1Dict["fluid pair"]
    liquidProperties = getFluidProperties(fluid, temperatures)
    vaporProperties = getFluidProperties(fluidPair, temperatures)

    value, conductivity, message = correlation(inputs2Dict, liquidProperties, vaporProperties)
else:
    fluidProperties = getFluidProperties(fluid, temperatures)

    value, conductivity, message = correlation(inputs2Dict, fluidProperties)

if value is not None:
    characteristicLength = inputs2Dict["characteristic length"]["result"]
    if isinstance(conductivity, (int, float)):
        result = value * conductivity / characteristicLength
        resultType = "h"
    elif conductivity == "k":
        result = value
        resultType = "k"
    else:
        result = value
        resultType = "h"
else:
    result = None
    resultType = None

# 8. Show results
showInputs(inputs1Dict, inputs2Dict)
showValidation(result, message)
showResults(result, resultType)