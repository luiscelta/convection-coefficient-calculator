def showInputs1Menu():
    print("-" * 60 + "\n" + " " * 20 + "FLOW, DOMAIN, GEOMETRIES" + " " * 20 + "\n" + "-" * 60 + """
    [1] Natural convection
        [1] Internal
            [1] Narrow vertical duct
                [1] Parallel plates
                [2] Circular
                [3] Squared
                [4] Equilateral triangle
            [2] Vertical rectangular cavity
            [3] Inclined rectangular cavity
            [4] Horizontal rectangular cavity
            [5] Spherical cavity
            [6] Concentric cylinders
            [7] Concentric spheres
        [2] External
            [1] Vertical flat plate
            [2] Inclined flat plate
            [3] Horizontal flat plate
            [4] Sphere
            [5] Vertical cylinder
            [6] Inclined cylinder
            [7] Horizontal cylinder
            [8] Sphere
    [2] Forced convection
        [1] Internal
            [1] Circular duct
            [2] Non-circular duct
                [1] Triangular
                [2] Rectangular (a/b = 1)
                [3] Rectangular (a/b = 1.43)
                [4] Rectangular (a/b = 2)
                [5] Rectangular (a/b = 3)
                [6] Rectangular (a/b = 4)
                [7] Rectangular (a/b = 8)
                [8] Rectangular (a/b >> 8)
            [3] Between parallel planes
            [4] Annular duct
                [1] Inner heat flow
                [2] Outer heat flow
                [3] Inner-outer heat flow
            [5] Helical coil
        [2] External
            [1] Flat plate
            [2] Cylinders with perpendicular flow
            [3] Other geometries with perpendicular flow
                [1] Square (face oriented)
                [2] Square (arist oriented)
                [3] Hexagon (face oriented)
                [4] Hexagon (arist oriented)
                [5] Rectangle (face oriented)
                [6] Ellipse (wide surface oriented)
                [6] Ellipse (narrow surface oriented)
            [4] Sphere
            [5] Cross-flow tube bundle
                [1] Square pitch
                [2] Triangular pitch
    [3] Natural condensation
        [1] Vertical flat surface
        [2] Inclined flat surface
        [3] Horizontal flat surface
            [1] Strip
            [2] Disk
        [4] Vertical cylinder
        [5] Inclined cylinder
        [6] Horizontal cylinder
        [7] Horizontal tube bundle
        [8] Sphere
    [4] Forced condensation
        [1] Internal
            [1] Circular duct
        [2] External
            [1] Horizontal cylinder
    [5] Natural boiling
    [6] Forced boiling
    
    """ + "\n" + "-" * 60 + "\n" + " " * 20 + "FLUIDS" + " " * 20 + "\n" + "-" * 60 + """

    [1] Air
    [2] Water (saturated liquid)
    [3] Water (saturated steam)
    [4] Ethylene glycol 20 %
    [5] Ethylene glycol 40 %
    [6] Propylene glycol 20 %
    [7] Propylene glycol 40 %
    [8] Thermal fluid Duratherm 600
    [9] Thermal fluid Duratherm LT
    [10] Butane (saturated liquid)
    [11] Butane (saturated steam)
    [12] Propane (saturated liquid)
    [13] Propane (saturated steam)
    [14] Carbon dioxide CO2 (saturated liquid)
    [15] Carbon dioxide CO2 (saturated steam)
    [16] Ammonia (saturated liquid)
    [17] Ammonia (saturated steam)
    [18] R-12 (saturated liquid)
    [19] R-12 (saturated steam)
    [20] R-22 (saturated liquid)
    [21] R-22 (saturated steam)
    [22] R-134a (saturated liquid)
    [23] R-134a (saturated steam)
    [24] R-404A (saturated liquid)
    [25] R-404A (saturated steam)
    [26] R-504A (saturated liquid)
    [27] R-504A (saturated steam)
    [28] R-508B (saturated liquid)
    [29] R-508B (saturated steam)

    """)


