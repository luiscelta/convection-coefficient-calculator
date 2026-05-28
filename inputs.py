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
    5: {"flow type": "Natural boiling", "domain type": None},
    6: {"flow type": "Forced boiling", "domain type": None},
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
    inputs1_dict = {
        "flow type": None,
        "domain type": None,
        "geometry1 type": None,
        "geometry2 type": None,
        "fluid": None
    }

    current = menu
    level_keys = ["flow type", "domain type", "geometry1 type", "geometry2 type"]

    while True:
        first_item = next(iter(current.values()))
        level_key = next(k for k in level_keys if k in first_item and first_item[k] is not None)

        print("-" * 60)
        for key, value in current.items():
            print(f"  [{key}] {value[level_key]}")
        print("-" * 60)

        choice = input("  Select an option: ").strip()
        if not choice.isdigit() or int(choice) not in current:
            print("  Invalid option.")
            continue

        selected = current[int(choice)]
        inputs1_dict[level_key] = selected[level_key]

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
        inputs1_dict["fluid"] = fluids[int(choice)]
        break

    return inputs1_dict


inputs1_dict = getInputs1(menu, fluids)
print(inputs1_dict)