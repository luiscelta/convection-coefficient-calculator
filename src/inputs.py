from math import cos, sin, radians


menu = {
    1: {
        "flow type": "Natural convection",
        "submenu": {
            1: {
                "domain type": "Internal",
                "submenu": {
                    1: {
                        "geometry1 type": "Narrow vertical duct",
                        "submenu": {
                            1: {"geometry2 type": "Parallel plates"},
                            2: {"geometry2 type": "Circular"},
                            3: {"geometry2 type": "Squared"},
                            4: {"geometry2 type": "Equilateral triangle"}
                        }
                    },
                    2: {"geometry1 type": "Vertical rectangular cavity"},
                    3: {"geometry1 type": "Inclined rectangular cavity"},
                    4: {"geometry1 type": "Horizontal rectangular cavity"},
                    5: {"geometry1 type": "Spherical cavity"},
                    6: {"geometry1 type": "Concentric cylinders"},
                    7: {"geometry1 type": "Concentric spheres"},
                }
            },
            2: {
                "domain type": "External",
                "submenu": {
                    1: {"geometry1 type": "Vertical flat plate"},
                    2: {"geometry1 type": "Inclined flat plate"},
                    3: {
                        "geometry1 type": "Horizontal flat plate",
                        "submenu": {
                            1: {"geometry2 type": "Hot top surface or cold bottom surface"},
                            2: {"geometry2 type": "Cold top surface or hot bottom surface"},
                        }
                    },
                    4: {"geometry1 type": "Sphere"},
                    5: {"geometry1 type": "Vertical cylinder"},
                    6: {"geometry1 type": "Inclined cylinder"},
                    7: {"geometry1 type": "Horizontal cylinder"},
                    8: {"geometry1 type": "Sphere"},
                }
            }
        }
    },
    2: {
        "flow type": "Forced convection",
        "submenu": {
            1: {
                "domain type": "Internal",
                "submenu": {
                    1: {"geometry1 type": "Circular duct"},
                    2: {
                        "geometry1 type": "Non-circular duct",
                        "submenu": {
                            1: {
                                "geometry2 type": "Triangular",
                                "submenu": {
                                    1: {"subtype": "Constant temperature"},
                                    2: {"subtype": "Constant heat flow"},
                                }
                            },
                            2: {
                                "geometry2 type": "Squared",
                                "submenu": {
                                    1: {"subtype": "Constant temperature"},
                                    2: {"subtype": "Constant heat flow"},
                                }
                            },
                            3: {
                                "geometry2 type": "Rectangular",
                                "submenu": {
                                    1: {"subtype": "Constant temperature"},
                                    2: {"subtype": "Constant heat flow"},
                                }
                            },
                        }
                    },
                    3: {"geometry1 type": "Between parallel planes"},
                    4: {
                        "geometry1 type": "Annular duct",
                        "submenu": {
                            1: {"geometry2 type": "Inner heat flow"},
                            2: {"geometry2 type": "Outer heat flow"},
                            3: {"geometry2 type": "Inner-outer heat flow"},
                        }
                    },
                    5: {"geometry1 type": "Helical coil"},
                }
            },
            2: {
                "domain type": "External",
                "submenu": {
                    1: {"geometry1 type": "Flat plate"},
                    2: {"geometry1 type": "Cylinders with perpendicular flow"},
                    3: {
                        "geometry1 type": "Other geometries with perpendicular flow",
                        "submenu": {
                            1: {"geometry2 type": "Square (face oriented)"},
                            2: {"geometry2 type": "Square (arist oriented)"},
                            3: {"geometry2 type": "Hexagon (face oriented)"},
                            4: {"geometry2 type": "Hexagon (arist oriented)"},
                            5: {"geometry2 type": "Rectangle (face oriented)"},
                            6: {"geometry2 type": "Ellipse (wide surface oriented)"},
                            7: {"geometry2 type": "Ellipse (narrow surface oriented)"},
                        }
                    },
                    4: {"geometry1 type": "Sphere"},
                    5: {
                        "geometry1 type": "Cross-flow tube bundle",
                        "submenu": {
                            1: {"geometry2 type": "Square pitch"},
                            2: {"geometry2 type": "Triangular pitch"},
                        }
                    },
                }
            }
        }
    },
    3: {
        "flow type": "Natural condensation",
        "domain type": None,
        "submenu": {
            1: {"geometry1 type": "Vertical flat surface"},
            2: {"geometry1 type": "Inclined flat surface"},
            3: {
                "geometry1 type": "Horizontal flat surface",
                "submenu": {
                    1: {"geometry2 type": "Strip"},
                    2: {"geometry2 type": "Disk"},
                    3: {"geometry2 type": "Other strip"},
                    4: {"geometry2 type": "Other disk"},
                }
            },
            4: {"geometry1 type": "Vertical cylinder"},
            5: {"geometry1 type": "Inclined cylinder"},
            6: {"geometry1 type": "Horizontal cylinder"},
            7: {"geometry1 type": "Horizontal tube bundle"},
            8: {"geometry1 type": "Sphere"},
        }
    },
    4: {
        "flow type": "Forced condensation",
        "submenu": {
            1: {
                "domain type": "Internal",
                "submenu": {
                    1: {"geometry1 type": "Circular duct"},
                }
            },
            2: {
                "domain type": "External",
                "submenu": {
                    1: {"geometry1 type": "Horizontal cylinder"},
                }
            }
        }
    },
    # 5: {"flow type": "Natural boiling", "domain type": None},
    # 6: {"flow type": "Forced boiling", "domain type": None},
}

fluids = {
    1: "Air",
    2: "Water (saturated liquid)",
    3: "Water (saturated vapor)",
    4: "Ethylene glycol 20%",
    5: "Ethylene glycol 40%",
    6: "Propylene glycol 20%",
    7: "Propylene glycol 40%",
    8: "Thermal fluid Duratherm 600",
    9: "Thermal fluid Duratherm LT",
    10: "Butane (saturated liquid)",
    11: "Butane (saturated vapor)",
    12: "Propane (saturated liquid)",
    13: "Propane (saturated vapor)",
    14: "Carbon dioxide CO2 (saturated liquid)",
    15: "Carbon dioxide CO2 (saturated vapor)",
    16: "Ammonia (saturated liquid)",
    17: "Ammonia (saturated vapor)",
    18: "R-12 (saturated liquid)",
    19: "R-12 (saturated vapor)",
    20: "R-22 (saturated liquid)",
    21: "R-22 (saturated vapor)",
    22: "R-134a (saturated liquid)",
    23: "R-134a (saturated vapor)",
    24: "R-404A (saturated liquid)",
    25: "R-404A (saturated vapor)",
    26: "R-504A (saturated liquid)",
    27: "R-504A (saturated vapor)",
    28: "R-508B (saturated liquid)",
    29: "R-508B (saturated vapor)",
}



fluidPairs = {
    "Water (saturated liquid)": "Water (saturated vapor)",
    "Butane (saturated liquid)": "Butane (saturated vapor)",
    "Propane (saturated liquid)": "Propane (saturated vapor)",
    "Carbon dioxide CO2 (saturated liquid)": "Carbon dioxide CO2 (saturated vapor)",
    "Ammonia (saturated liquid)": "Ammonia (saturated vapor)",
    "R-12 (saturated liquid)": "R-12 (saturated vapor)",
    "R-22 (saturated liquid)": "R-22 (saturated vapor)",
    "R-134a (saturated liquid)": "R-134a (saturated vapor)",
    "R-404A (saturated liquid)": "R-404A (saturated vapor)",
    "R-504A (saturated liquid)": "R-504A (saturated vapor)",
    "R-508B (saturated liquid)": "R-508B (saturated vapor)",
}





def getInputs1(menu, fluids):
    inputs1Dict = {
        "flow type": None,
        "domain type": None,
        "geometry1 type": None,
        "geometry2 type": None,
        "subtype": None,
        "fluid": None,
        "fluid pair": None
    }

    current = menu
    levelKeys = ["flow type", "domain type", "geometry1 type", "geometry2 type", "subtype"]

    while True:
        firstItem = next(iter(current.values()))
        levelKey = next(k for k in levelKeys if k in firstItem and firstItem[k] is not None)

        print("-" * 60)
        for key, value in current.items():
            print(f"  [{key}] {value[levelKey]}")
        print("-" * 60)

        choice = input("  Select an option: ").strip()
        if not choice.isdigit() or int(choice) not in current:
            print("  Invalid option.")
            continue

        selected = current[int(choice)]
        inputs1Dict[levelKey] = selected[levelKey]

        if selected.get("submenu") is None:
            break

        current = selected["submenu"]

    

    isCondensation = inputs1Dict["flow type"] in ["Natural condensation", "Forced condensation"]

    if isCondensation:
        filteredFluids = [v for v in fluids.values() if v in fluidPairs]
        availableFluids = {i + 1: v for i, v in enumerate(filteredFluids)}
    else:
        availableFluids = fluids

    print("-" * 60)
    for key, value in availableFluids.items():
        print(f"  [{key}] {value}")
    print("-" * 60)

    while True:
        choice = input("  Select a fluid: ").strip()
        if not choice.isdigit() or int(choice) not in availableFluids:
            print("  Invalid option.")
            continue
        inputs1Dict["fluid"] = availableFluids[int(choice)]
        if inputs1Dict["flow type"] in ["Natural condensation", "Forced condensation"]:
            inputs1Dict["fluid pair"] = fluidPairs[inputs1Dict["fluid"]]
        break

    return inputs1Dict


    


parameters = {
    ("Natural convection", "Internal", "Narrow vertical duct", "Parallel plates", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "coefficient": 1/192},
    ("Natural convection", "Internal", "Narrow vertical duct", "Circular", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "coefficient": 1/128},
    ("Natural convection", "Internal", "Narrow vertical duct", "Squared", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "coefficient": 1/113.6},
    ("Natural convection", "Internal", "Narrow vertical duct", "Equilateral triangle", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "coefficient": 1/106.4},
    ("Natural convection", "Internal", "Vertical rectangular cavity", None, None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]}},
    ("Natural convection", "Internal", "Inclined rectangular cavity", None, None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]},
                                                               "angle": None},
    ("Natural convection", "Internal", "Horizontal rectangular cavity", None, None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]},
                                                               "top surface": None,
                                                               "angle": 0},
    ("Natural convection", "Internal", "Spherical cavity", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural convection", "Internal", "Concentric cylinders", None, None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"inner diameter": None, "outer diameter": None, "result": lambda d: (d["outer diameter"] - d["inner diameter"]) / 2}},
    ("Natural convection", "Internal", "Concentric spheres", None, None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"inner diameter": None, "outer diameter": None, "result": lambda d: (d["outer diameter"] - d["inner diameter"]) / 2}},
    ("Natural convection", "External", "Vertical flat plate", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural convection", "External", "Inclined flat plate", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural convection", "External", "Horizontal flat plate", "Hot top surface or cold bottom surface", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural convection", "External", "Horizontal flat plate", "Cold top surface or hot bottom surface", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural convection", "External", "Sphere", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural convection", "External", "Vertical cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "diameter": None, "result": lambda d: d["length"]}},
    ("Natural convection", "External", "Inclined cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "diameter": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural convection", "External", "Horizontal cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Forced convection", "Internal", "Circular duct", None, None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"length": None, "inner diameter": None, "result": lambda d: d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Triangular", "Constant temperature"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Triangular", "Constant heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Squared", "Constant temperature"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Squared", "Constant heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular", "Constant temperature"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"long side": None, "short side": None, "ratio": lambda d: d["long side"] / d["short side"], "area": lambda d: d["long side"] * d["short side"], "perimeter": lambda d: 2 * d["long side"] + 2 * d["short side"], "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular", "Constant heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"long side": None, "short side": None, "ratio": lambda d: d["long side"] / d["short side"], "area": lambda d: d["long side"] * d["short side"], "perimeter": lambda d: 2 * d["long side"] + 2 * d["short side"], "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Between parallel planes", None, None): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"length": None, "separation": None, "result": lambda d: 2 * d["separation"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Inner heat flow", None): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"length": None, "inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Outer heat flow", None): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"length": None, "inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Inner-outer heat flow", None): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"length": None, "inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Helical coil", None, None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"inner diameter": None, "coil diameter": None, "result": lambda d: d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Flat plate", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Cylinders with perpendicular flow", None, None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Square (face oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Square (arist oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Hexagon (face oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Hexagon (arist oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Rectangle (face oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Ellipse (wide surface oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Ellipse (narrow surface oriented)", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Sphere", None, None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Cross-flow tube bundle", "Square pitch", None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"outer diameter": None, "x1": None, "result": lambda d: d["outer diameter"]},
                                                               "fluid velocity": {"inlet velocity": None},
                                                               "number of columns": None},
    ("Forced convection", "External", "Cross-flow tube bundle", "Triangular pitch", None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"outer diameter": None, "x1": None, "x2": None, "x3": None, "result": lambda d: d["outer diameter"]},
                                                               "fluid velocity": {"inlet velocity": None},
                                                               "number of columns": None},
    ("Natural condensation", None, "Vertical flat surface", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Inclined flat surface", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural condensation", None, "Horizontal flat surface", "Strip", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Horizontal flat surface", "Disk", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural condensation", None, "Horizontal flat surface", "Other strip", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural condensation", None, "Horizontal flat surface", "Other disk", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural condensation", None, "Vertical cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Inclined cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "angle": None},
    ("Natural condensation", None, "Horizontal cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural condensation", None, "Horizontal tube bundle", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "number of rows": None},
    ("Natural condensation", None, "Sphere", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Forced condensation", "Internal", "Circular duct", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "inlet vapor velocity": None,
                                                               "vapor quality": {"inlet": None, "outlet": None}},
    ("Forced condensation", "External", "Horizontal cylinder", None, None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "vapor velocity": None},
}






def getInputs2(data2Dict):
    for key, value in data2Dict.items():
        if isinstance(value, dict):
            print(f"\n  {key}:")
            for subKey, subValue in value.items():
                if subValue is None:
                    while True:
                        try:
                            value[subKey] = float(input(f"    {subKey}: "))
                            break
                        except ValueError:
                            print("    Invalid input.")
        elif value is None:
            while True:
                try:
                    data2Dict[key] = float(input(f"\n  {key}: "))
                    break
                except ValueError:
                    print("  Invalid input.")

    
     # 2. Calcular lambdas automáticamente
    for key, value in data2Dict.items():
        if isinstance(value, dict):
            for subKey, subValue in value.items():
                if callable(subValue):
                    value[subKey] = subValue(value)



    return data2Dict



if __name__ == "__main__":
    inputs1Dict = getInputs1(menu, fluids)
    keyTupleInputs = (inputs1Dict["flow type"], inputs1Dict["domain type"], inputs1Dict["geometry1 type"], inputs1Dict["geometry2 type"], inputs1Dict["subtype"])
    data2Dict = parameters[keyTupleInputs] 
    inputs2Dict = getInputs2(data2Dict)
    print(inputs1Dict)
    print(inputs2Dict)