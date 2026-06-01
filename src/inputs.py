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
                    3: {"geometry1 type": "Horizontal flat plate"},
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
                            1: {"geometry2 type": "Triangular"},
                            2: {"geometry2 type": "Rectangular (a/b = 1)"},
                            3: {"geometry2 type": "Rectangular (a/b = 1.43)"},
                            4: {"geometry2 type": "Rectangular (a/b = 2)"},
                            5: {"geometry2 type": "Rectangular (a/b = 3)"},
                            6: {"geometry2 type": "Rectangular (a/b = 4)"},
                            7: {"geometry2 type": "Rectangular (a/b = 8)"},
                            8: {"geometry2 type": "Rectangular (a/b >> 8)"},
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
                    3: {"geometry2 type": "Other"},
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
    3: "Water (saturated steam)",
    4: "Ethylene glycol 20%",
    5: "Ethylene glycol 40%",
    6: "Propylene glycol 20%",
    7: "Propylene glycol 40%",
    8: "Thermal fluid Duratherm 600",
    9: "Thermal fluid Duratherm LT",
    10: "Butane (saturated liquid)",
    11: "Butane (saturated steam)",
    12: "Propane (saturated liquid)",
    13: "Propane (saturated steam)",
    14: "Carbon dioxide CO2 (saturated liquid)",
    15: "Carbon dioxide CO2 (saturated steam)",
    16: "Ammonia (saturated liquid)",
    17: "Ammonia (saturated steam)",
    18: "R-12 (saturated liquid)",
    19: "R-12 (saturated steam)",
    20: "R-22 (saturated liquid)",
    21: "R-22 (saturated steam)",
    22: "R-134a (saturated liquid)",
    23: "R-134a (saturated steam)",
    24: "R-404A (saturated liquid)",
    25: "R-404A (saturated steam)",
    26: "R-504A (saturated liquid)",
    27: "R-504A (saturated steam)",
    28: "R-508B (saturated liquid)",
    29: "R-508B (saturated steam)",
}


def getInputs1(menu, fluids):
    inputs1Dict = {
        "flow type": None,
        "domain type": None,
        "geometry1 type": None,
        "geometry2 type": None,
        "fluid": None
    }

    current = menu
    levelKeys = ["flow type", "domain type", "geometry1 type", "geometry2 type"]

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

    print("-" * 60)
    for key, value in fluids.items():
        print(f"  [{key}] {value}")
    print("-" * 60)

    while True:
        choice = input("  Select a fluid: ").strip()
        if not choice.isdigit() or int(choice) not in fluids:
            print("  Invalid option.")
            continue
        inputs1Dict["fluid"] = fluids[int(choice)]
        break

    return inputs1Dict



def getMaxVelocitySquareTubeBundle(d):
    
    inletVelocity = d["fluid velocity"]["inlet velocity"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    x1 = d["characteristic length"]["x1"]
    
    # Operación matemática limpia
    v_max = inletVelocity * (x1 / (x1 - outerDiameter))
    
    # Guardamos el resultado en su sitio
    d["fluid velocity"]["max velocity"] = v_max
    

def getMaxVelocityTriangularTubeBundle(d):
    
    inletVelocity = d["fluid velocity"]["inlet velocity"]
    outerDiameter = d["characteristic length"]["outer diameter"]
    x1 = d["characteristic length"]["x1"]
    x3 = d["characteristic length"]["x3"]

    if 2 * (x3 - outerDiameter) >= x1 - outerDiameter:
        v_max = inletVelocity * x1 / (x1 - outerDiameter)
    
    else:
        v_max = inletVelocity * x1 / (2 * (x3 - outerDiameter))

    
    # Guardamos el resultado en su sitio
    d["fluid velocity"]["max velocity"] = v_max






parameters = {
    ("Natural convection", "Internal", "Narrow vertical duct", "Parallel plates"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "separation": None, "result": lambda d: 2 * d["separation"]}},
    ("Natural convection", "Internal", "Narrow vertical duct", "Circular"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]}},
    ("Natural convection", "Internal", "Narrow vertical duct", "Squared"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]}},
    ("Natural convection", "Internal", "Narrow vertical duct", "Equilateral triangle"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]}},
    ("Natural convection", "Internal", "Vertical rectangular cavity", None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]}},
    ("Natural convection", "Internal", "Inclined rectangular cavity", None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]},
                                                               "angle": None},
    ("Natural convection", "Internal", "Horizontal rectangular cavity", None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"length": None, "width": None, "result": lambda d: d["width"]},
                                                               "top surface": None,
                                                               "bottom surface": None},
    ("Natural convection", "Internal", "Spherical cavity", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural convection", "Internal", "Concentric cylinders", None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"inner diameter": None, "outer diameter": None, "result": lambda d: (d["outer diameter"] - d["inner diameter"]) / 2}},
    ("Natural convection", "Internal", "Concentric spheres", None): {"temperatures": {"surface 1": None, "surface 2": None, "mean": lambda d: (d["surface 1"] + d["surface 2"]) / 2},
                                                               "characteristic length": {"inner diameter": None, "outer diameter": None, "result": lambda d: (d["outer diameter"] - d["inner diameter"]) / 2}},
    ("Natural convection", "External", "Vertical flat plate", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural convection", "External", "Inclined flat plate", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural convection", "External", "Horizontal flat plate", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural convection", "External", "Sphere", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural convection", "External", "Vertical cylinder", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "diameter": None, "result": lambda d: d["length"]}},
    ("Natural convection", "External", "Inclined cylinder", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "diameter": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural convection", "External", "Horizontal cylinder", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Forced convection", "Internal", "Circular duct", None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"inner diameter": None, "result": lambda d: d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Triangular"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 1)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 1.43)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 2)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 3)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 4)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b = 8)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Non-circular duct", "Rectangular (a/b >> 8)"):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: 4 * d["area"] / d["perimeter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Between parallel planes", None):  {"temperatures": {"fluid": None},
                                                               "characteristic length": {"separation": None, "result": lambda d: 2 * d["separation"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Inner heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"duct length": None,"inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Outer heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"duct length": None,"inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Annular duct", "Inner-outer heat flow"): {"temperatures": {"fluid": None},
                                                               "characteristic length": {"duct length": None,"inner diameter": None, "outer diameter": None, "result": lambda d: d["outer diameter"] - d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "Internal", "Helical coil", None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"inner diameter": None, "coil diameter": None, "result": lambda d: d["inner diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Flat plate", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"plate length": None, "result": lambda d: d["plate length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Cylinders with perpendicular flow", None): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Square (face oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Square (arist oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Hexagon (face oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Hexagon (arist oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Rectangle (face oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Ellipse (wide surface oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Other geometries with perpendicular flow", "Ellipse (narrow surface oriented)"): {"temperatures": {"fluid": None, "surface": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Sphere", None): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "fluid velocity": None},
    ("Forced convection", "External", "Cross-flow tube bundle", "Square pitch"): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"outer diameter": None, "x1": None, "result": lambda d: d["outer diameter"]},
                                                               "fluid velocity": {"inlet velocity": None, "max velocity": "calculated"},
                                                               "calculate": [getMaxVelocitySquareTubeBundle]},
    ("Forced convection", "External", "Cross-flow tube bundle", "Triangular pitch"): {"temperatures": {"fluid": None, "surface": None},
                                                               "characteristic length": {"outer diameter": None, "x1": None, "x2": None, "x3": None, "result": lambda d: d["outer diameter"]},
                                                               "fluid velocity": {"inlet velocity": None, "max velocity": "calculated"},
                                                               "calculate": [getMaxVelocityTriangularTubeBundle]},
    ("Natural condensation", None, "Vertical flat surface", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Inclined flat surface", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]},
                                                               "angle": None},
    ("Natural condensation", None, "Horizontal flat surface", "Strip"): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Horizontal flat surface", "Disk"): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural condensation", None, "Horizontal flat surface", "Other"): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"area": None, "perimeter": None, "result": lambda d: d["area"] / d["perimeter"]}},
    ("Natural condensation", None, "Vertical cylinder", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"length": None, "result": lambda d: d["length"]}},
    ("Natural condensation", None, "Inclined cylinder", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "angle": None},
    ("Natural condensation", None, "Horizontal cylinder", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Natural condensation", None, "Horizontal tube bundle", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "number of tubes": None},
    ("Natural condensation", None, "Sphere", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]}},
    ("Forced condensation", "Internal", "Circular duct", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "inlet vapor velocity": None,
                                                               "vapor quality": {"inlet": None, "outlet": None}},
    ("Forced condensation", "External", "Horizontal cylinder", None): {"temperatures": {"fluid": None, "surface": None, "saturation": None, "film": lambda d: (d["fluid"] + d["surface"]) / 2},
                                                               "characteristic length": {"diameter": None, "result": lambda d: d["diameter"]},
                                                               "vapor velocity": None}
    # ("Natural boiling", None, None, None): None,
    # ("Forced boiling", None, None, None): None,
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

    
    if "calculate" in data2Dict:
        for function in data2Dict["calculate"]:
            function(data2Dict)


    return data2Dict



if __name__ == "__main__":
    inputs1Dict = getInputs1(menu, fluids)
    keyTupleInputs = (inputs1Dict["flow type"], inputs1Dict["domain type"], inputs1Dict["geometry1 type"], inputs1Dict["geometry2 type"])
    data2Dict = parameters[keyTupleInputs] 
    inputs2Dict = getInputs2(data2Dict)
    print(inputs1Dict)
    print(inputs2Dict)