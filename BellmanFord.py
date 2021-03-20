import logging

# Bellmand Ford Algorithm Python implemantion 
# Calculates the shortest path from a node to all other nodes

# Algorithm overview
# Computation data requires leading, trailing node and connecting Link
# Operations include access of leading, trailing and connecting link
# Addition arithmetic, comparison, and write to memory

# Reasoning for the implementation of Node list data structure       
# There can be two ways to store the structure for the list of nodes aand their values
# For example, the node number identification can be stored with the link data structure
# This will reduce the additional access to retrieve the node value from an alternative node
# data structure
# However, this also breaks the flexibility when passing pre-processed links from an API to BMF
# For example, with the above implementation, we essentially use the memory address of the link
# as a replacement for the node number such that when we access a link we also access the node
# This means that the pre-processor must insert the link in the same position as that of the node number
# This ofcourse comparitively removes the flexibility of cosntructing the link data structure
# using randomized positions
# Therefore we have chosen to decouple the link data structure and node list data structure
# And sacrificing an additional access for the leading node


# 1) Modeling the graphical data structure
# We define the graphical links using a class Data structure
# Attach the leading node address, Link value and Trailing node address as Attributes

class Link:
    
    def __init__(self, leading_address, link_value, trailing_address):
        #Initialize the initial values of the Link structure
        self.leading_node_address = leading_address
        self.link_value = link_value
        self.trailing_node_address = trailing_address

#Encapsulation of data structures and operations related to Bellmand Ford
#Allows decoupling from main execution code
class BellmandFord:

    # Graph structure is defined external to the class
    # Node values data structure is defined in class

    def __init__(self, link_list, num_of_nodes, start_node):
        self.graph_structure = link_list
        self.num_of_nodes = num_of_nodes

        # Declare and initialize the data structure for node values
        # All values will default initialize to infinity except starting node 
        # Starting node initilized to 0 to determine starting point of BMF 

        self.node_list = [float('inf')]* num_of_nodes
        self.node_list[start_node-1] = 0

    def show_nodes(self):
        for node in self.node_list:
            print("Node no: %s, value: %s" % (str(self.node_list.index(node) + 1), str(node)))

    def loop_graph(self):
        for link in self.graph_structure:
            print("Link value: " + str(link.link_value))

    # An instance of implementation for the Bellmand Ford algorithm solver
    # Performs check for the infinite condition defined by default initialization
    # Loops through link list, computes leading ndoe and link value and overwrites trailing node if value is less
    def solve(self):
        for x in range(self.num_of_nodes-1):
            print("Iteration: ", x)
            for link in self.graph_structure:
                try:
                    if not (self.node_list[link.leading_node_address-1] == float('inf')):
                        if(self.node_list[link.leading_node_address-1] + link.link_value < self.node_list[link.trailing_node_address-1]):
                            print("Change calculated for node: ", str(link.trailing_node_address))
                            print("(node no: %s, value: %s + link value: %s) < (node no: %s, value: %s)" % (str(link.leading_node_address), str(self.node_list[link.leading_node_address-1]), str(link.link_value), str(link.trailing_node_address), str(self.node_list[link.trailing_node_address-1])))
                            self.node_list[link.trailing_node_address-1] = self.node_list[link.leading_node_address-1] + link.link_value
                        else:
                            print("No change in node values calculated")
                            self.show_nodes()
                    else:
                        raise Exception('Selected link with infinite value')
                except Exception: 
                        print("Selected link with infinite value, skipped: %s -> %s" % (str(link.leading_node_address), str(link.trailing_node_address)))
                    #logging.exception("Handled exception, selected infinite link. Link skipped")
                


 
 # Pre-processor of data required for Bellmand Ford Algorithm
 #Serialization of data from API, possibly JSON
 #Determine the number of nodes
 #Structuring of data from API can be encapsulated in class structure to provide
 #decoupling for modularity design
 #When the pre-processor changes, this is independent of the Bellmand operation
 #Therefore the pre-processor can be repalced without affecting the implementation of BMF
 #Only requirements are that the data types are satified for BMF instantiation 


# Instantiation of Links
test_link = Link(5, 10, 2)
link_1 = Link(1, 10, 2)
link_2 = Link(1, 20, 3)
link_3 = Link(1, 7, 4)
link_4 = Link(2, 5, 3)


# --Reasoning, can be skipped--
# When creating the structure of the links which define the graphical structure, the order defined defines the order of computation
# However, it may not be possible to always order links under columns defined in the graph structure
# For example, to define links with columns, we partition the links in layers (1,2), (1,3), (1,4) may be in the same column
# (3,5) may reside in a different column
# Because of this problem, we must perform checks on the value of the leading node in the initial iteration
# If we access a value of infinity, we have accessed a link in a further column in the graph structure

# --Analysis of the link computation sequence-- can be skipped
# The performance of the algorithm depends strongly on the ordering of the links
# The greater the number of infinite links selected, the lower the performance of the algorithm
# Consider the links containing the intial starting node placed at the end of the link data structure
# This creates the worst possible performance, since we will select all infinite links until a non-infinite node value
# If enough infinite links are selected, it may be worth implementing a pre-processor to provide re-ordered links to the BMF instance
# An alternative solution may be to implement a faster search for the link data structure instead of linear search

# list formation defines the graphical structure and the computation order
list_link_from_API = [test_link, link_2, link_1, link_3, link_4]
determined_num_nodes = 5
determined_start_node = 1

#Create an instance of a Bellmand Ford operation
BellmandFordOperation = BellmandFord(list_link_from_API, determined_num_nodes, determined_start_node)
BellmandFordOperation.solve()








