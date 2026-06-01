from unittest.mock import patch
import pytest
from src.inputs import menu, fluids, parameters, getInputs1, getInputs2


# ==================== TESTS getInputs1 ====================

getInputs1_cases = [
    # (inputs, expected)
    (["1", "1", "1", "1", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Narrow vertical duct", "geometry2 type": "Parallel plates", "fluid": "Air"}),
    (["1", "1", "1", "2", "3"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Narrow vertical duct", "geometry2 type": "Circular", "fluid": "Water (saturated steam)"}),
    (["1", "1", "2", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Vertical rectangular cavity", "geometry2 type": None, "fluid": "Air"}),
    (["1", "1", "3", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Inclined rectangular cavity", "geometry2 type": None, "fluid": "Air"}),
    (["1", "2", "1", "1"], {"flow type": "Natural convection", "domain type": "External", "geometry1 type": "Vertical flat plate", "geometry2 type": None, "fluid": "Air"}),
    (["1", "2", "7", "1"], {"flow type": "Natural convection", "domain type": "External", "geometry1 type": "Horizontal cylinder", "geometry2 type": None, "fluid": "Air"}),
    (["2", "1", "1", "1"], {"flow type": "Forced convection", "domain type": "Internal", "geometry1 type": "Circular duct", "geometry2 type": None, "fluid": "Air"}),
    (["2", "1", "2", "1", "1"], {"flow type": "Forced convection", "domain type": "Internal", "geometry1 type": "Non-circular duct", "geometry2 type": "Triangular", "fluid": "Air"}),
    (["2", "1", "4", "3", "1"], {"flow type": "Forced convection", "domain type": "Internal", "geometry1 type": "Annular duct", "geometry2 type": "Inner-outer heat flow", "fluid": "Air"}),
    (["2", "2", "3", "1", "1"], {"flow type": "Forced convection", "domain type": "External", "geometry1 type": "Other geometries with perpendicular flow", "geometry2 type": "Square (face oriented)", "fluid": "Air"}),
    (["2", "2", "5", "1", "1"], {"flow type": "Forced convection", "domain type": "External", "geometry1 type": "Cross-flow tube bundle", "geometry2 type": "Square pitch", "fluid": "Air"}),
    (["3", "1", "1"], {"flow type": "Natural condensation", "domain type": None, "geometry1 type": "Vertical flat surface", "geometry2 type": None, "fluid": "Air"}),
    (["3", "3", "1", "1"], {"flow type": "Natural condensation", "domain type": None, "geometry1 type": "Horizontal flat surface", "geometry2 type": "Strip", "fluid": "Air"}),
    (["3", "3", "3", "1"], {"flow type": "Natural condensation", "domain type": None, "geometry1 type": "Horizontal flat surface", "geometry2 type": "Other", "fluid": "Air"}),
    (["4", "1", "1", "1"], {"flow type": "Forced condensation", "domain type": "Internal", "geometry1 type": "Circular duct", "geometry2 type": None, "fluid": "Air"}),
    (["4", "2", "1", "1"], {"flow type": "Forced condensation", "domain type": "External", "geometry1 type": "Horizontal cylinder", "geometry2 type": None, "fluid": "Air"}),
    (["1", "2", "1", "29"], {"flow type": "Natural convection", "domain type": "External", "geometry1 type": "Vertical flat plate", "geometry2 type": None, "fluid": "R-508B (saturated steam)"}),
    (["abc", "1", "1", "1", "1", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Narrow vertical duct", "geometry2 type": "Parallel plates", "fluid": "Air"}),
    (["99", "1", "1", "1", "1", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Narrow vertical duct", "geometry2 type": "Parallel plates", "fluid": "Air"}),
    (["", "1", "1", "1", "1", "1"], {"flow type": "Natural convection", "domain type": "Internal", "geometry1 type": "Narrow vertical duct", "geometry2 type": "Parallel plates", "fluid": "Air"}),
]

@pytest.mark.parametrize("inputs, expected", getInputs1_cases)
def test_getInputs1(inputs, expected):
    with patch("builtins.input", side_effect=inputs):
        result = getInputs1(menu, fluids)
    for key, value in expected.items():
        assert result[key] == value


# ==================== TESTS getInputs2 ====================

getInputs2_cases = [
    # (key_tupla, inputs, checks)
    (("Natural convection", "Internal", "Narrow vertical duct", "Parallel plates"),
     ["25", "80", "0.5", "0.01"],
     {"temperatures.fluid": 25.0, "temperatures.surface": 80.0, "temperatures.film": 52.5,
      "characteristic length.separation": 0.01, "characteristic length.result": 0.02}),

    (("Natural convection", "Internal", "Narrow vertical duct", "Circular"),
     ["25", "80", "0.5", "0.0025", "0.2"],
     {"characteristic length.result": 4 * 0.0025 / 0.2}),

    (("Natural convection", "Internal", "Vertical rectangular cavity", None),
     ["60", "40", "1.0", "0.05"],
     {"temperatures.mean": 50.0, "characteristic length.result": 0.05}),

    (("Natural convection", "Internal", "Inclined rectangular cavity", None),
     ["60", "40", "1.0", "0.05", "30"],
     {"angle": 30.0}),

    (("Natural convection", "External", "Vertical flat plate", None),
     ["25", "80", "0.5"],
     {"temperatures.film": 52.5, "characteristic length.result": 0.5}),

    (("Forced convection", "Internal", "Circular duct", None),
     ["25", "80", "0.02", "10"],
     {"characteristic length.result": 0.02}),

    (("Forced convection", "External", "Cross-flow tube bundle", "Square pitch"),
     ["25", "80", "0.05", "15", "20"],
     {"characteristic length.result": 0.05, "fluid velocity.max velocity": 20.0 * (15.0 / (15.0 - 0.05))}),

    (("Natural condensation", None, "Vertical flat surface", None),
     ["25", "80", "100", "0.5"],
     {"temperatures.saturation": 100.0, "temperatures.film": 52.5, "characteristic length.result": 0.5}),

    (("Forced condensation", "Internal", "Circular duct", None),
     ["25", "80", "100", "0.05", "10", "0.5", "0.3"],
     {"characteristic length.result": 0.05, "vapor quality.inlet": 0.5, "vapor quality.outlet": 0.3}),
]

@pytest.mark.parametrize("key, inputs, checks", getInputs2_cases)
def test_getInputs2(key, inputs, checks):
    data = parameters[key]
    with patch("builtins.input", side_effect=inputs):
        result = getInputs2(data)
    for path, expected_value in checks.items():
        parts = path.split(".")
        value = result
        for part in parts:
            value = value[part]
        assert value == expected_value