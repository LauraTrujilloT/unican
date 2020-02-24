# Introduction to parallel programming
February 24 2020

- To speed up computation we move from a single processor to multiple processors.
- Sequential programming paradigms are not able to exploit these extra resources optimally.

- We need programming models designed to exploit parallelism.

- These models allow for one or various processors to work in common in solving a common computational task

## Challenges

- Synchronisation
- Communication among tasks
- Race conditions (multiple processes are said to be in race conditions if their results depend on the order of execution, data corruption)
- Increased complexity

## Tasks

- A complex problem is divided in a number of tasks that represent computational work.
- Task granularity reflects the size of each task and how independent they are of each other.


## Scheduling

- Process of assigning tasks to processes or threads and giving them an execution ordering.
- It can be performed at: (i) cooling time, (ii) compilation time, (iii) dynamically at execution time.
- It requires to take into account independency among tasks.


## Load balancing

- Practice and techniques for distributing fare shares of work among tasks (objective will be to have them busy as long as possible)
- Homogenous
- Heterogenous

## Parallel slowdown

- When throwing further resources into the problem results in loger execution times.
- Typically due to communications bottlenecks.
- The algorithm implementation causes communications overheads when new node are added.
- At some point these overhead are bigger than the reduction of overall computional time.

# Parallel programming models

- By problem decomposition (data parallelism, task parallelism, implicit parallelism Automatic parallelism)
- By process interaction (shared memory, message passing, implicit interaction FPLs, DSLs)

## Models by problem decomposition

- Data parallelism (Each processor performs the same task on different data, not only in HPC also in distributed computing, some big data software packages: MapReduce, Apache Spark)
- Task parallelism (each processors performs a different task on the same data)
- Implicit parallelism (automatic parallelisation: loops for instance, compilers)


