# High-Performance Computing: Supercomputing

##Outline

- Computer basics
- Supercomputer : applications, performance, evolution, cooling
- Example of supercomputer: _Altamira_

## Introduction

**CPU (Central Processing Unit)**: microscopic transistors. Each operation requires three stages: Fetch (instruction from RAM), decode,execute.

**RAM (Random Access Memory)**: System's short term data storage. It allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory.

The main difference between other storage devices is that time required to load or write data depends on the physical location.

## Computational science applied in physics

- First application in modern computers
- Applications in accelerator physics, astrophysics, fluid mechanics, computational fluid dynamics, nuclear engineering computer codes and so on.

**Some history**

Babbage's machine $\rightarrow$ Zuse's VersuchsModell 1 $\rightarrow$ Enigma $\rightarrow$ Colossus (first electronic computer) $\rightarrow$ Apple I (4kB RAM) $\rightarrow$ IBM PC 5150 (16kB RAM)

### Introduction to parallelism

- Individual processors are not capable of solving some computational problems
- Solution: put several processors to work to solve the same problem
- The advent of supercomputers pushed parallelism
- Microprocessors made possible to build machines with many cheap processors that could work together.

## Supercomputer

A lot of hardware in a big room!

Basically, it is a group of computers that act as one collective machine and it provides close to the best currently achievable sustained performance on demanding computational problems.

> Scientific and engineering **applications** that must handle very large databases or do a great amount of computation: Quantum mechanics, weather forecasting, climate research, physics simulations, HUGE impact in cryptanalysis.

### Supercomputing (SC) Applications !

There are a lot of.

> Look for algorithm of blockchains related to cryptocurrency.

- SpiNNaker : SC project to simulate human brain

### Performance

- **Fl** oating point **Op** erations per **s** econd (FLOP/s)
- **Rmax**: real maximal performance achieved on the LINPACK benchmark
- **Rpeak**: theoretical maximum performance measured in GFlops (can never be reached, LINPACK benchmark is used by TOP 500 : measures how fast a computer can perform a n equations)
- **Speedup**: Improvement in speed of execution of a task executed on two similar architectures with different resources. (related to [Amdhal's law](https://www.sciencedirect.com/topics/computer-science/amdahls-law))

$$Speedup = \frac{1}{(1-p) + p/N } $$

being N the number of processors and p the part of parallizable code.

### Cooling

- Extreme speed of a supercomputer is "converted" to extreme heat (_the faster the hotter_)
- The aim is to keep the servers running at its most efficient operating temperature.
- As well, the cluster is quite inefficient when cold.

### Types of cooling systems

- **air cooling** system: method of dissipating heat through fans
- **Water cooling** system: use water to remove waste geat from servers
- **Free cooling** system: using low external air temperatures to assist in chilling water.

### Example: Altamira
- In 2006 Barcelona Supercomputing Center (BSC) update their supercomputer called marenostrum.
- First version of Altamira was installed in 2007 thanks to BSC
- It is located in IFCA (_Instituto de Física de Cantabria_)
- In addition to RES (_Red Española de Supercomputación_), Altamira currently gives support to UC users and other national projects.

#### Some applications of Altamira
- Climate Change (_Santander Meteorology Group_): modeling the climate system (with a grid).
- TRUFA (Transcriptomes User-Friendly Analysis)

### General Parallel File system
A **parallel file system** also known as a clustered file system, is a type of storage system designed to store data across multiple networked servers and to facilitate high-performance access through simultaneous, coordinated input/output operations between clients and storage nodes.

**GPFS** is high performance clustered file system software used to distribute and manage data across multiple servers, developed by IBM. Now it is called _Spectrum Scale_ and it has become the leading file systems for HPC applications.

### Infiniband network

Infiniband (IB) is a computer-networking communication standard used in high.performance computing that features very high throughput and very low latency.

- Used in the interconnection between servers and storage systems.
- Remote direct memory Access
- Low power consumption

### Batch Processing systems

Computerized batch processing is the running of jobs that can run without end user interaction, or can be scheduled to run as resources permit.

- Control the access to the resources
- Schedule the shared computer resources among users and programs.
- Queues associated to same-featured resources and purpose
- Jobs are sorted according to a priority scheme.
- Large jobs must be submitted to the cluster through the batch system.
- Example of batch system schedulers: Torque, Sun Grid Engine, Slurm.

#### Slurm

_Slurm_ is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small linux clusters.

Some key functions:

1. It allocates exclusive or non-exclusive access to compute nodes to users for some duration of time so they can execute computational tasks.
2.  It provides a series of commands starting
