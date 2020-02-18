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
