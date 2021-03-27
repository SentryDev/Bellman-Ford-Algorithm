# Bellman-Ford-Algorithm
Python implementation of Bellman Ford algorithm

# Bellmand Ford Algorithm Python implemantion 
Calculates the shortest path from a vertex to all other vertices and identifies a negative cycle.
The Bellman Ford is mainly used for cycle idenitfication rather than a more efficient shortest path algorithm.

# Algorithm overview
Computation data requires leading, trailing node and connecting Link

Operations include access of leading, trailing and connecting link

Addition arithmetic, comparison, and write to memory

# Algorithm overview
Time complexity O(EV), for complete graphs O(V^3)

# Documentation
In this documentation, we show an implementation of the Bellman Ford using Python and provide a reasoned methodology for the design decisions.

# Implementation of Node list data structure       
There can be two ways to store the structure for the list of nodes aand their values.

For example, the node number identification can be stored with the link data structure
This will reduce the additional access to retrieve the node value from an alternative node
data structure. However, this also breaks the flexibility when passing pre-processed links from an API to BMF.
For example, with the above implementation, we essentially use the memory address of the link
as a replacement for the node number such that when we access a link we also access the node.
This means that the pre-processor must insert the link in the same position as that of the node number.
This ofcourse comparitively removes the flexibility of cosntructing the link data structure
using randomized positions.
Therefore, we have chosen to decouple the link data structure and node list data structure and sacrificing an additional access for the leading node

# Infinite link value check
When creating the structure of the links which define the graphical structure, the order defined defines the order of computation.
However, it may not be possible to always order links such all selected values are non-infinite
For example, consider the links ordered (1,2), (1,3), (1,4), (4,3) and choosing the starting node to be 4. With this ordering of links, we selecte 3 infinite value links before the starting node link value can be selected.
Because of this problem, we must perform checks on the value of the leading node in the initial iteration.
If we access a value of infinity, we have accessed a link in a further column in the graph structure and therefore can be skipped.

# Analysis of the link computation sequence
The performance of the algorithm depends strongly on the ordering of the links.
The greater the number of infinite links selected, the lower the performance of the algorithm.
Consider the links containing the intial starting node placed at the end of the link data structure,
this creates the worst possible performance since we will select all infinite links until a non-infinite node value.
If enough infinite links are selected, it may be worth implementing a pre-processor to provide re-ordered links to the BMF instance.
An alternative solution may be to implement a faster search for the link data structure instead of linear search.
Although in any case, we implement for the worst possible case which occurs when iterating V-1 times.






