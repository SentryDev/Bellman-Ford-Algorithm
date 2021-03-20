# Bellman-Ford-Algorithm
Python implementation of Bellman Ford algorithm

# Bellmand Ford Algorithm Python implemantion 
Calculates the shortest path from a node to all other nodes

# Algorithm overview
Computation data requires leading, trailing node and connecting Link
Operations include access of leading, trailing and connecting link
Addition arithmetic, comparison, and write to memory

# Implementation of Node list data structure       
There can be two ways to store the structure for the list of nodes aand their values
For example, the node number identification can be stored with the link data structure
This will reduce the additional access to retrieve the node value from an alternative node
data structure
However, this also breaks the flexibility when passing pre-processed links from an API to BMF
For example, with the above implementation, we essentially use the memory address of the link
as a replacement for the node number such that when we access a link we also access the node
This means that the pre-processor must insert the link in the same position as that of the node number
This ofcourse comparitively removes the flexibility of cosntructing the link data structure
using randomized positions
Therefore we have chosen to decouple the link data structure and node list data structure
And sacrificing an additional access for the leading node

# Infinite link value check
When creating the structure of the links which define the graphical structure, the order defined defines the order of computation
However, it may not be possible to always order links under columns defined in the graph structure
For example, to define links with columns, we partition the links in layers (1,2), (1,3), (1,4) may be in the same column
(3,5) may reside in a different column
Because of this problem, we must perform checks on the value of the leading node in the initial iteration
If we access a value of infinity, we have accessed a link in a further column in the graph structure

# Analysis of the link computation sequence
The performance of the algorithm depends strongly on the ordering of the links
The greater the number of infinite links selected, the lower the performance of the algorithm
Consider the links containing the intial starting node placed at the end of the link data structure
This creates the worst possible performance, since we will select all infinite links until a non-infinite node value
If enough infinite links are selected, it may be worth implementing a pre-processor to provide re-ordered links to the BMF instance
An alternative solution may be to implement a faster search for the link data structure instead of linear search






