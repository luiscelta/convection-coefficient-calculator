from inputs import menu, fluids, parameters, getInputs1, getInputs2
from fluids import getFluidProperties
from selector import getCorrelation
from results import showInputs, showResults

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
# 5. Get fluid properties
temperatures = inputs2Dict["temperatures"]
fluidProperties = getFluidProperties(fluid, temperatures)

# 6. Get correlation and execute
correlation = getCorrelation(keyTupleInputs)

if inputs1Dict["fluid pair"] is not None:
    pairFluid = inputs1Dict["fluid pair"]
    if "(saturated liquid)" in fluid:
        liquidProperties = fluidProperties
        vaporProperties = getFluidProperties(pairFluid, temperatures)
    else:
        vaporProperties = fluidProperties
        liquidProperties = getFluidProperties(pairFluid, temperatures)
    result = correlation(inputs2Dict, liquidProperties, vaporProperties)
else:
    result = correlation(inputs2Dict, fluidProperties)

# 7. Show results
showInputs(inputs1Dict, inputs2Dict)
showResults(result)