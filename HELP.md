# Input Data Reference

This document describes the input data requested by the program for each problem type. All temperatures are in °C, lengths in m, areas in m², velocities in m/s, and angles in degrees.

---

## 1. Natural Convection

### 1.1 Internal

#### 1.1.1 Narrow vertical duct

##### 1.1.1.1 Parallel plates / 1.1.1.2 Circular / 1.1.1.3 Squared / 1.1.1.4 Equilateral triangle

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: duct length [m]
- **area**: cross-section area [m²]
- **perimeter**: cross-section perimeter [m]

#### 1.1.2 Vertical rectangular cavity

- **surface 1**: temperature of surface 1 [°C]
- **surface 2**: temperature of surface 2 [°C]
- **length**: cavity height [m]
- **width**: cavity width (gap between surfaces) [m]

#### 1.1.3 Inclined rectangular cavity

- **surface 1**: temperature of surface 1 [°C]
- **surface 2**: temperature of surface 2 [°C]
- **length**: cavity height [m]
- **width**: cavity width (gap between surfaces) [m]
- **angle**: inclination angle from horizontal [°]

#### 1.1.4 Horizontal rectangular cavity

- **surface 1**: temperature of surface 1 [°C]
- **surface 2**: temperature of surface 2 [°C]
- **length**: cavity length [m]
- **width**: cavity width (gap between surfaces) [m]
- **top surface**: which surface is on top (1 or 2)

#### 1.1.5 Spherical cavity

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **diameter**: cavity diameter [m]

#### 1.1.6 Concentric cylinders

- **surface 1**: temperature of surface 1 [°C]
- **surface 2**: temperature of surface 2 [°C]
- **inner diameter**: inner cylinder diameter [m]
- **outer diameter**: outer cylinder diameter [m]

#### 1.1.7 Concentric spheres

- **surface 1**: temperature of surface 1 [°C]
- **surface 2**: temperature of surface 2 [°C]
- **inner diameter**: inner sphere diameter [m]
- **outer diameter**: outer sphere diameter [m]

---

### 1.2 External

#### 1.2.1 Vertical flat plate

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: plate height [m]

#### 1.2.2 Inclined flat plate

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: plate length [m]
- **angle**: inclination angle from vertical [°]

#### 1.2.3 Horizontal flat plate

##### 1.2.3.1 Hot top surface or cold bottom surface / 1.2.3.2 Cold top surface or hot bottom surface

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **area**: plate surface area [m²]
- **perimeter**: plate perimeter [m]

#### 1.2.4 Sphere

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **diameter**: sphere diameter [m]

#### 1.2.5 Vertical cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: cylinder height [m]
- **diameter**: cylinder diameter [m]

#### 1.2.6 Inclined cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: cylinder length [m]
- **diameter**: cylinder diameter [m]
- **angle**: inclination angle from vertical [°]

#### 1.2.7 Horizontal cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **diameter**: cylinder diameter [m]

---

## 2. Forced Convection

### 2.1 Internal

#### 2.1.1 Circular duct

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: duct length [m]
- **inner diameter**: duct inner diameter [m]
- **fluid velocity**: mean fluid velocity [m/s]

#### 2.1.2 Non-circular duct

##### 2.1.2.1 Triangular (Constant temperature / Constant heat flow)

- **fluid**: fluid temperature [°C]
- **area**: cross-section area [m²]
- **perimeter**: cross-section perimeter [m]
- **fluid velocity**: mean fluid velocity [m/s]

##### 2.1.2.2 Squared (Constant temperature / Constant heat flow)

- **fluid**: fluid temperature [°C]
- **area**: cross-section area [m²]
- **perimeter**: cross-section perimeter [m]
- **fluid velocity**: mean fluid velocity [m/s]

##### 2.1.2.3 Rectangular (Constant temperature / Constant heat flow)

- **fluid**: fluid temperature [°C]
- **long side**: long side of the rectangular cross-section [m]
- **short side**: short side of the rectangular cross-section [m]
- **fluid velocity**: mean fluid velocity [m/s]

#### 2.1.3 Between parallel planes

- **fluid**: fluid temperature [°C]
- **length**: length of the planes in the direction of fluid flow [m]
- **separation**: distance between planes [m]
- **fluid velocity**: mean fluid velocity [m/s]

#### 2.1.4 Annular duct

##### 2.1.4.1 Inner heat flow / 2.1.4.2 Outer heat flow / 2.1.4.3 Inner-outer heat flow

###### Inner heat flow: heat flow through the surface of the inner duct, with the surface of the outer duct insulated
###### Outer heat flow: heat flow through the surface of the outer duct, with the surface of the inner duct insulated
###### Inner-outer heat flow: heat flow through the surface of the inner and outer duct

- **fluid**: fluid temperature [°C]
- **length**: duct length [m]
- **inner diameter**: inner duct outer diameter [m]
- **outer diameter**: outer duct inner diameter [m]
- **fluid velocity**: mean fluid velocity [m/s]

#### 2.1.5 Helical coil

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **inner diameter**: tube inner diameter [m]
- **coil diameter**: coil diameter [m]
- **fluid velocity**: mean fluid velocity [m/s]

---

### 2.2 External

#### 2.2.1 Flat plate

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **length**: plate length in flow direction [m]
- **fluid velocity**: free-stream velocity [m/s]

#### 2.2.2 Cylinders with perpendicular flow

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **diameter**: cylinder diameter [m]
- **fluid velocity**: free-stream velocity [m/s]

#### 2.2.3 Other geometries with perpendicular flow

##### 2.2.3.1 Square (face oriented) / 2.2.3.2 Square (arist oriented) / 2.2.3.3 Hexagon (face oriented) / 2.2.3.4 Hexagon (arist oriented) / 2.2.3.5 Rectangle (face oriented) / 2.2.3.6 Ellipse (wide surface oriented) / 2.2.3.7 Ellipse (narrow surface oriented)

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **fluid velocity**: free-stream velocity [m/s]

###### Square (face oriented)
- **length**: length of one side [m]
###### Square (arist oriented)
- **length**: length of the diagonal [m]
###### Hexagon (face oriented)
- **length**: width across corners [m]
###### Hexagon (arist oriented)
- **length**: width across flats [m]
###### Rectangle (face oriented)
- **length**: length of the long side [m]
###### Ellipse (wide surface oriented)
- **length**: major axis [m]
###### Ellipse (narrow surface oriented)
- **length**: minor axis [m]


#### 2.2.4 Sphere

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **diameter**: sphere diameter [m]
- **fluid velocity**: free-stream velocity [m/s]

#### 2.2.5 Cross-flow tube bundle

##### 2.2.5.1 Square pitch

- **fluid**: fluid temperature [°C]
- **surface**: tube surface temperature [°C]
- **outer diameter**: tube outer diameter [m]
- **x1**: distance between the centers of two adjacent tubes in a column perpendicular to the fluid flow direction (transversal pitch) [m]
- **x2**: distance between the centers of two adjacent tubes in a row parallel to the fluid flow direction (longitudinal pitch) [m]
- **inlet velocity**: fluid velocity at bundle inlet [m/s]
- **number of columns**: number of tube columns in the flow direction

##### 2.2.5.2 Triangular pitch

- **fluid**: fluid temperature [°C]
- **surface**: tube surface temperature [°C]
- **outer diameter**: tube outer diameter [m]
- **x1**: distance between the centers of two adjacent tubes in a column perpendicular to the fluid flow direction (transversal pitch) [m]
- **x2**: distance between the centers of two adjacent tubes in a row parallel to the fluid flow direction (longitudinal pitch) [m]
- **x3**: distance between the centers of two adjacent tubes in consecutive diagonal rows (diagonal pitch) [m]
- **inlet velocity**: fluid velocity at bundle inlet [m/s]
- **number of columns**: number of tube columns in the flow direction

---

## 3. Natural Condensation

#### 3.1 Vertical flat surface

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **length**: surface height [m]

#### 3.2 Inclined flat surface

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **length**: surface length [m]
- **angle**: inclination angle from horizontal [°]

#### 3.3 Horizontal flat surface

##### 3.3.1 Strip

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **length**: strip width (smaller dimension) [m]

##### 3.3.2 Disk

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: disk diameter [m]

##### 3.3.3 Other strip / 3.3.4 Other disk

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **area**: surface area [m²]
- **perimeter**: surface perimeter [m]

#### 3.4 Vertical cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: cylinder diameter [m]
- **length**: cylinder height [m]

#### 3.5 Inclined cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: cylinder diameter [m]
- **angle**: inclination angle from horizontal [°]

#### 3.6 Horizontal cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: cylinder diameter [m]

#### 3.7 Horizontal tube bundle

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: tube diameter [m]
- **number of rows**: number of tube rows

#### 3.8 Sphere

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: sphere diameter [m]

---

## 4. Forced Condensation

### 4.1 Internal

#### 4.1.1 Circular duct

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: inner duct diameter [m]
- **inlet vapor velocity**: vapor velocity at duct inlet [m/s]
- **inlet**: inlet vapor quality (0 to 1)
- **outlet**: outlet vapor quality (0 to 1)

### 4.2 External

#### 4.2.1 Horizontal cylinder

- **fluid**: fluid temperature [°C]
- **surface**: surface temperature [°C]
- **saturation**: saturation temperature [°C]
- **diameter**: cylinder outer diameter [m]
- **vapor velocity**: vapor free-stream velocity [m/s]
