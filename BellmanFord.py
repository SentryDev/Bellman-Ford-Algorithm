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

    def __init__(self, link_list):
            self.graph_structure = link_list

    def loop_graph(self):
        for link in self.graph_structure:
            print("Link value: " + str(link.link_value))


# Instantiation of links
# Structuring of data from API should be encapsulated in class structure to provide
# decoupling, this separates the computational data and the operations on the data
# Non-API Instantiation of Links
link_1 = Link(6, 10, 2)
link_2 = Link(4, 5, 3)
link_3 = Link(7, 7, 4)

# list formation defines the graphical structure
list_link_from_API = [link_1, link_2, link_3]

#Create an instance of a Bellmand Ford operation
BellmandFordOperation = BellmandFord(list_link_from_API)
BellmandFordOperation.loop_graph()

