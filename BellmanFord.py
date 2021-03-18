# Bellmand Ford Algorithm calculates the shortest path form a node to all other nodes

# Algorithm overview
# Computation data requires leading, trailing node and connecting Link
# Operations include access of leading, trailing and connecting link
# Addition arithmetic, comparison, and write to memory


# 1) Modeling the graphical data structure
# We define the graphical links using a class Data structure
# Attach the leading node value, Link value and Trailing node address as Attributes

# We store the value of the leading node and not the address, this allwos us to 
# Reduce the additional access required in the Node value data structure

class Link:
    
    def __init__(self, leading_value, link_value, trailing_address):
        #Initialize the initial values of the Link structure
        self.leading_value = leading_value
        self.link_value = link_value
        self.trailing_address = trailing_address

#Encapsulation of data structures and operation related to Bellmand Ford
#Allows decoupling from main execution code
class BellmandFord:

    # Graph structure is defined external to the class
    # Node values data structure is defined in class
    def __init__(self, link_list, num_of_nodes):
        self.graph_structure = link_list

        # Declare and initialize the data structure for node values
        self.list_nodes = []

    def loop_graph(self):
        for link in self.graph_structure:
            print("Link value: " + str(link.link_value))

    # An instance of implementation for the Bellmand Ford algorithm
    def solve(self):
        for link in self.graph_structure:
            if(link.leading_value + link.link_value < node[link.trailing_value]):
                
        

# Pre-processor of data required for Bellmand Ford Algorithm
# Serialization of data from API, possibly JSON
# Determine the number of nodes
# Structuring of data from API can be encapsulated in class structure to provide
# decoupling for modularity design
# When the pre-processor changes, this is independent of the Bellmand operation
# Therefore the pre-processor can be repalced without affecting the implementation of BMF
# Only requirements are that the data types are satified for BMF instantiation

# Instantiation of Links
link_1 = Link(6, 10, 2)
link_2 = Link(4, 5, 3)
link_3 = Link(7, 7, 4)

# list formation defines the graphical structure
list_link_from_API = [link_1, link_2, link_3]
determined_num_nodes = 9

#Create an instance of a Bellmand Ford operation
BellmandFordOperation = BellmandFord(list_link_from_API, determined_num_nodes)
BellmandFordOperation.loop_graph()

