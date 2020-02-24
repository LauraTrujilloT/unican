# Triggers

## DAQ (Data Acquisition)

It is a specialized engineering discipline thriving mostly in the eco-system of large science experiments, particularly in HEP. It consists mainly of electronics, computer science, networking and a little bit of physics.

The DAQ system collects the data from the _different parts of the detector_, converts the data in a suitable format and saves it to _permanent storage_.

## DAQ/Trigger

Trigger **must** : 
- Select with high efficiency signal(s) of interest. (Need to be able to precisely calculate trigger efficiency, avoid biases affecting physics results, rejected events are loss for ever!)
- Achieve high background rejection. (reduce rate to match DAQ and offline computing capabilities)
- Be affordable. (limited custom electronics and computing power imply that trigger algorithms must be design to have a fast execution time)

The DAQ **must**:

- Provide online services (run control systems, data flow monitoring)
- Keep record of data taking and detector conditions.
- avoid data corruption and data loss, check data integrity.
- Be robust against varying data taking conditions and detector/electronics problems.
- Provide flexibility to record data in different configuration. (Commissioning, calibration)


