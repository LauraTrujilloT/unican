# <p align="center"> Geant 4 Examples </p>
<p align="center">Clara Lasaosa  <a href="mailto: clara.lasaosa@alumnos.unican.es">clara.lasaosa@alumnos.unican.es </a> </p> </p>
<p align="center">Laura Trujillo <a href="mailto: lvtrujillot@unal.edu.co">lvtrujillot@unal.edu.co </a> </p>
<p align="center"> February 24th, 2020 </p>

## Introduction

The purpose of the exercise is to simulate the passage of particles through matter by means of the toolkit Geant4 that stands for GEometry And Tracking and uses Monte Carlo methods. It includes facilities for handling geometry and tracking among others, so that an analysis of the physical layout of the experiment (e.g. detectors, absorbers, etc) considering how this layout will affect the path of particles in the experiment, as well as a simulation of the passage of a particle through matter considering possible interactions and decay processes can be carried out.

Two examples have been done. The first of them simulates a simplified fixed target experiment where the primary kinematics consists of a single proton which hits the target perpendicular to the entrance face. On the other hand, the second one simulates schematically a positron emitted tomography system where the default particle beam is an ion, at rest, randomly distributed within a zone inside a patient.

### Installation

The OS used for the installation of _Geant4_ was _Ubuntu 18.04_ and it was necessary the installation of some packages described below,

```shell
$ sudo apt-get install libxerces-c-dev qt4-dev-tools freeglut3-dev libmotif-dev tk-dev cmake libxpm-dev libxmu-dev libxi-dev
```

Then, a directory called _geant4_ in the path `/opt/applications` was created.

```shell
$ cd /opt/ ; sudo mkdir /applications; cd applications/
$ sudo mkdir geant4
```

Afterwards,it was proceeded with the downloading of [Geant4](Ohttp://geant4.web.cern.ch/support/source/geant4.10.04.p01.tar.gz), unpacking and creation of `geant4-build` directory,

```shell
$ sudo mv ~/Path/to/geant4.10.04.p01.tar.gz /opt/applications/geant4/.
$ cd /opt/applications/geant4/
$ sudo tar -xvzf geant4.10.04.p01.tar.gz
$ mkdir geant4.10.04.p01-build
```

Here `~/Path/to/` is the direction where it was downloaded the `.tar` file. Last, it is required to configure the build and run `CMake`.

```shell
$ mkdir geant4.10.04.p01-build ; cd geant4.10.04.p01-build
$ sudo cmake -DCMAKE_INSTALL_PREFIX=/opt/applications/geant4/geant4.10.04.p01-install -DGEANT4_USE_GDML=ON -DCMAKE_BUILD_TYPE=Debug -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_XM=ON -DGEANT4_USE_QT=ON -DGEANT4_BUILD_MULTITHREADED=ON /opt/applications/geant4/geant4.10.04.p01
$ make -jN
$ make install -jN
```
> `N` refers to the number of cores available in the pc (i.e `make -j4`)


Finally, for `bash` users:

```shell
$ vim ~/.bashrc

#geant4
source /opt/applications/geant4/geant4.10.04.p01-install/bin/geant4.sh
```

For `zsh` users, the `source` could be written in the `.zshrc` as well. If any errors appears, best thing to do is _source_ from the directory of installation (`.../geant4-install/bin/geant4.sh`)

### Running an example in _Geant4_

Create a folder and copy one of the examples in that directory.

```shell
$ mkdir ~/workspace
$ mkdir ~/workspace/G4WORK
$ cp -R ~/geant4/geant4.10.04.p01/examples/basic/B1/ ~/workspace/G4WORK/.
```
To compile,

```shell
$ cd ~/workspace/G4WORK/
$ mkdir B1-build
$ cd B1-build
$ cmake ../B1
$ make -jN
$ ./exampleB1
```

## Results:

_This example simulated a simplified fixed target experiment_

### B2a

_Geometry definition:_ Regarding the geometry of the first example, the set-up consists of a target followed by six chambers of increasing transverse size at defined instances from the target. They are located in a region called the Tracker region and their shapes are cylinders.

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

Material| Density [mg/cm3] |  RadL|Nucl.Int.Length [m]| Imean [eV] | Temperature [K] | Pressure [atm]
-----------|-------------|------------|-------|-------|----|----|
G4_AIRm    | 1.205        | 303.921|  710.095 | 85.700 |293.15| 1.00
G4_Pb| 11.350 |5.613| 0.18248| 823.000| 293.15 | 1.00
<p align="center"> <i>Table 1a. Some materials example B2a </i> </p>

## Example B3

_This example simulates schematically a positron emitted tomography system_


### B3a

_Geometry definition_:In regard to the set-up geometry corresponding to the second example, scintillating crystals are used for gamma detection. The crystals are described by a matrix and are circularly arranged to form a ring. Few rings make up the full detector.


Parameters | Values |
-----------|--------|
`globalField`| off|
`gun/energy`| 1.0 eV|
`gun/particle`| e+ |
`run/beamOn`| 100 (Fig. 3) |
<p align="center"> <i>Table 2. Parameters modified example B3a </i> </p>

![Figura 3](b3a-2.png =200x)
<p align="center"> <i>Figure 3. Front view of detector for 100 Events </i> </p>

Material| Density [mg/cm3] |  RadL [m]|Nucl.Int.Length [m]| Imean [eV] | Temperature [K] | Pressure [atm]
-----------|-------------|------------|-------|-------|----|----|
G4_BRAIN_ICRP   | 1.040| 0.35403|0.72156 | 73.300 |293.15| 1.00
G4_AIR| 1.205 |303.921| 710.095| 85.700| 293.15 | 1.00
<p align="center"> <i>Table 2a. Some materials example B3a </i> </p>


The `output` obtained: `The run was 100 events ; Nb of 'good' e+ annihilations: 16
Total dose in patient : 1.25761 picoGy`
