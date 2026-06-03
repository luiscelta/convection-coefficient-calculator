import pytest
from src.fluids import FluidProperties, getFluidProperties


fluidProperties_cases = [
    # (fluid, temperatures, checks)
    # checks: dict of "temp_key.property" -> expected_value

    ("Air",
     {"fluid": 50.0, "surface": 100.0, "film": 75.0},
     {
         "fluid.density": 1.299 - 4.073e-3 * 50 + 7.362e-6 * 50**2 - 5.08e-9 * 50**3,
         "fluid.specificHeat": (1.006 + 8.52e-6 * 50 + 5.33e-7 * 50**2 - 4.03e-10 * 50**3) * 1000,
         "film.dynamicViscosity": (17.334 + 0.0466 * 75 - 1.54e-5 * 75**2) * 1e-6,
         "surface.conductivity": (24.399 + 0.0673 * 100 - 8.77e-6 * 100**2) * 1e-3,
         "fluid.surfaceTension": None,
         "fluid.latentHeat": None,
     }),

    ("Water (saturated liquid)",
     {"fluid": 25.0, "surface": 80.0, "film": 52.5},
     {
         "fluid.density": 1001 - 0.178 * 25 - 2.57e-3 * 25**2,
         "film.specificHeat": (4.208 - 9.68e-4 * 52.5 + 8.26e-6 * 52.5**2 + 1.81e-8 * 52.5**3) * 1000,
         "surface.dynamicViscosity": (1773.5 - 51.81 * 80 + 0.821 * 80**2 - 6.966e-3 * 80**3 + 2.929e-5 * 80**4 - 4.77e-8 * 80**5) * 1e-6,
         "fluid.surfaceTension": (77.167 - 0.191 * 25) * 1e-3,
         "fluid.latentHeat": None,
     }),

    ("Water (saturated vapor)",
     {"fluid": 100.0},
     {
         "fluid.density": -0.379 + 0.0193 * 100 - 3.39e-4 * 100**2 + 3.17e-6 * 100**3 - 1.01e-8 * 100**4 + 2.71e-11 * 100**5,
         "fluid.latentHeat": (2456.6 - 1.31 * 100 - 6.49e-3 * 100**2) * 1000,
         "fluid.surfaceTension": None,
     }),

    ("Ethylene glycol 20%",
     {"film": 40.0},
     {
         "film.density": 1035.7 - 0.248 * 40 - 2.44e-3 * 40**2,
         "film.specificHeat": (3.769 + 2.3e-3 * 40) * 1000,
         "film.surfaceTension": None,
     }),

    ("Butane (saturated liquid)",
     {"fluid": 20.0},
     {
         "fluid.density": 600.8 - 1.09 * 20 - 1.57e-3 * 20**2,
         "fluid.surfaceTension": (14.92 - 0.123 * 20) * 1e-3,
         "fluid.latentHeat": None,
     }),

    ("Butane (saturated vapor)",
     {"fluid": 20.0},
     {
         "fluid.density": 2.748 + 0.0974 * 20 + 1.4e-3 * 20**2 + 8.84e-6 * 20**3,
         "fluid.latentHeat": (384.5 - 0.904 * 20 - 2.14e-3 * 20**2) * 1000,
         "fluid.surfaceTension": None,
     }),

    ("Ammonia (saturated liquid)",
     {"fluid": -10.0, "surface": 30.0},
     {
         "fluid.density": 638.6 - 1.38 * (-10) - 2.42e-3 * (-10)**2,
         "surface.surfaceTension": (33.408 - 0.337 * 30) * 1e-3,
         "fluid.latentHeat": None,
     }),

    ("R-134a (saturated liquid)",
     {"film": 25.0},
     {
         "film.density": 1295 - 3.39 * 25 - 8.12e-3 * 25**2,
         "film.conductivity": 0.092 - 4.49e-4 * 25 + 4.06e-7 * 25**2,
         "film.surfaceTension": (11.733 - 0.143 * 25) * 1e-3,
     }),

    ("R-134a (saturated vapor)",
     {"film": 25.0},
     {
         "film.density": 14.211 + 0.5 * 25 + 7.75e-3 * 25**2 + 5.8e-5 * 25**3,
         "film.latentHeat": (198.6 - 0.787 * 25 - 2.66e-3 * 25**2) * 1000,
         "film.surfaceTension": None,
     }),

    ("R-508B (saturated liquid)",
     {"fluid": -50.0},
     {
         "fluid.density": 997.9 - 8.72 * (-50) - 0.0297 * (-50)**2,
         "fluid.surfaceTension": (0.82 - 0.118 * (-50) + 3.26e-4 * (-50)**2) * 1e-3,
     }),

    ("R-508B (saturated vapor)",
     {"fluid": -50.0},
     {
         "fluid.density": 212.061 + 6.77 * (-50) + 0.0808 * (-50)**2 + 3.44e-4 * (-50)**3,
         "fluid.latentHeat": (75 - 1.6 * (-50) - 6.43e-3 * (-50)**2) * 1000,
     }),
]


@pytest.mark.parametrize("fluid, temperatures, checks", fluidProperties_cases)
def test_getFluidProperties(fluid, temperatures, checks):
    results = getFluidProperties(fluid, temperatures)

    # Verifica que devuelve las mismas claves
    assert set(results.keys()) == set(temperatures.keys())

    # Verifica que cada valor es FluidProperties
    for key in results:
        assert isinstance(results[key], FluidProperties)

    # Verifica valores calculados
    for path, expected in checks.items():
        temp_key, prop = path.split(".")
        value = getattr(results[temp_key], prop)
        if expected is None:
            assert value is None
        else:
            assert value == pytest.approx(expected)