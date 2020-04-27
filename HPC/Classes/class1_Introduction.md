# High Performance Computing (HPC) : Introduction

HPC is based in _parallel computing_ which uses many cores at the same time.

**Overview**
- HPC System Layout
- HPC Architectures

## HPC System Layout
- Nodes (CPUs) connected together via network
- Each node has independet memory and OS

### Anatomy of a computer

**1. Central Processing Unit (CPU)**: It does all the computation with basic instructions such as: `+,-,*,/, AND, OR` and others. (It computes all of this through electronic components, it means, through hardware rather than software)

**2. Random-Access Memory (RAM)**: Any part of memory can be read and retrieved at random. It keeps track of all information that the CPU needs and the OS controls it and gives pieces of it to software that requires for it, _i.e_ numbers, strings, any data needed to be store somewhere.

## HPC: Architectures

### Distributed Memory Architectures
- Multiple CPUs working together
- Clusters and interconnects.
- Performance of parallel computing depends also on _interconnect_ Performance

**Client/Server**

- Workload distributed between a server.
- Server usually process one task upon a client request.
- Normally, the communication is through a network

**peer-to-peer**

- Workload distributed between different members of the network (aka peers).
- There are not fixed clients nor servers.
- Decentralized architecture.
- All nodes can have the same role.

### Hybrid Architectures

-

## HPC: Infrastructures

### Clusters

It has several nodes (CPUs) connected between them through network (or some other interconnection) acting like an unique or coherent system so that a higher performance is obtained and higher storage capacity as well. It is also known as _batch processing_.

The common **components** of a cluster are:  Frontend(access nodes), computing nodes, network connection, distributed storage, resource manager (manages resources from nodes) and a queue manager (assign priorities to user requests). Clusters can be used for HPC as well as for HTC (High Throughput Computing)

The common **usages** for a cluster are:

- Research and industry
- Completing computing tasks complicated enough to be done with a single CPU.

### Grid Computing

It is a global distributed access to computing and storage resources. It is basically a way of providing access to local HTC clusters through network.

However, it **requires** more control by the end-user. Its main use is academic projects where local HPC clusters are connected and shared either national or international level.

### Cloud computing

This method employs the internet as a basis for "cycles" as a service. It provides dynamic and scalable resources to the end-user as service (normally, you have to pay for it).

### e-Infrastructures

- e-Infrastructures provide digital services for research and innovation.

- It addresses the needs of European researchers for digital services in terms of networking, computing and data management.
