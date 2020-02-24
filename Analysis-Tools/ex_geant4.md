# <p align="center"> Geant 4 Examples </p>
<p align="center">Clara Lasaosa  <a href="mailto: lvtrujillot@unal.edu.co">clara.lasaosa@alumnos.unican.es </a> </p> </p>
<p align="center">Laura Trujillo <a href="mailto: lvtrujillot@unal.edu.co">lvtrujillot@unal.edu.co </a> </p>
<p align="center"> February 24th, 2020 </p>

## Example B2:

_This example simulated a simplified fixed target experiment_

### B2a

List of parameters modified in the example:

Parameters | Values |
-----------|--------|
`globalField`| 2.0 T|
`gun/energy`| 1.0 GeV|
`gun/particle`| p |
`run/beamOn`| 1 (Fig. 1), 100 (Fig. 2) |
<p align="center"> <i>Table 1. Parameters modified example B2a </i> </p>

![Figura 1](b2a-1.png =200x)
<p align="center"> <i>Figure 1. Side view of detector for 1 Event </i> </p>

![Figura 2](b2a-2.png =200x)
<p align="center"> <i>Figure 2. Side view of detector for 100 Events </i> </p>

## Example B3

_This example simulates schematically a positron emitted tomography system_

_Geometry definition_: Scintillating crystals are used for gamma detection. In this example, the crystals are described by a matrix and are circularly arranged to form a ring.

### B3a

Parameters | Values |
-----------|--------|
`globalField`| off|
`gun/energy`| 1.0 eV|
`gun/particle`| e+ |
`run/beamOn`| 100 (Fig. 3) |
<p align="center"> <i>Table 2. Parameters modified example B3a </i> </p>

![Figura 3](b3a-2.png =200x)
<p align="center"> <i>Figure 3. Front view of detector for 100 Events </i> </p>

The `output` obtained: `The run was 100 events ; Nb of 'good' e+ annihilations: 16
Total dose in patient : 1.25761 picoGy`
