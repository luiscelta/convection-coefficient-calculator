import pytest
from src.dimensionless import calculateReynolds, calculatePrandtl, calculateGrashof, calculateRayleigh


reynolds_cases = [
    # (density, velocity, characteristicLength, dynamicViscosity, expected)
    (1.0, 10.0, 0.5, 1e-5, 1.0 * 10.0 * 0.5 / 1e-5),
    (998.0, 2.0, 0.02, 1e-3, 998.0 * 2.0 * 0.02 / 1e-3),
    (1.2, 5.0, 1.0, 1.8e-5, 1.2 * 5.0 * 1.0 / 1.8e-5),
]

@pytest.mark.parametrize("density, velocity, cl, mu, expected", reynolds_cases)
def test_calculateReynolds(density, velocity, cl, mu, expected):
    assert calculateReynolds(density, velocity, cl, mu) == pytest.approx(expected)


prandtl_cases = [
    # (dynamicViscosity, specificHeat, conductivity, expected)
    (1.8e-5, 1006.0, 0.026, 1.8e-5 * 1006.0 / 0.026),
    (1e-3, 4182.0, 0.606, 1e-3 * 4182.0 / 0.606),
    (0.001, 2000.0, 0.5, 0.001 * 2000.0 / 0.5),
]

@pytest.mark.parametrize("mu, cp, k, expected", prandtl_cases)
def test_calculatePrandtl(mu, cp, k, expected):
    assert calculatePrandtl(mu, cp, k) == pytest.approx(expected)


grashof_cases = [
    # (temperatures, cl, mu, density, expected)
    # Caso con film temperature
    ({"fluid": 25.0, "surface": 80.0, "film": 52.5},
     0.5, 1.8e-5, 1.1,
     9.81 * (1 / (52.5 + 273.15)) * abs(80.0 - 25.0) * 0.5**3 / (1.8e-5 / 1.1)**2),

    # Caso con mean temperature
    ({"surface 1": 60.0, "surface 2": 40.0, "mean": 50.0},
     0.05, 1e-3, 998.0,
     9.81 * (1 / (50.0 + 273.15)) * abs(60.0 - 40.0) * 0.05**3 / (1e-3 / 998.0)**2),

    # Caso con g custom
    ({"fluid": 20.0, "surface": 100.0, "film": 60.0},
     1.0, 2e-5, 1.0,
     9.81 * (1 / (60.0 + 273.15)) * abs(100.0 - 20.0) * 1.0**3 / (2e-5 / 1.0)**2),
]

@pytest.mark.parametrize("temperatures, cl, mu, density, expected", grashof_cases)
def test_calculateGrashof(temperatures, cl, mu, density, expected):
    assert calculateGrashof(temperatures, cl, mu, density) == pytest.approx(expected)


rayleigh_cases = [
    (1e6, 0.71, 1e6 * 0.71),
    (5e8, 7.0, 5e8 * 7.0),
    (100.0, 0.5, 100.0 * 0.5),
]

@pytest.mark.parametrize("grashof, prandtl, expected", rayleigh_cases)
def test_calculateRayleigh(grashof, prandtl, expected):
    assert calculateRayleigh(grashof, prandtl) == pytest.approx(expected)