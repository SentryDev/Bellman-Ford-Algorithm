# Bellmand Ford Algorithm calculates the shortest path form a node to all other nodes

# Algorithm overview
# Computation data requires leading, trailing node and connecting Link
# Operations include access of leading, trailing and connecting link
# Addition arithmetic, comparison, and write to memory


# 1) Modeling the graphical data structure
# We define the graphical links using a class Data structure
# Attach the leading node value, Link value and Trailing node address as Attributes

class Link:
    
    def __init__(self, leading_value, link_value, trailing_address):
        #Initialize the initial values of the Link structure
        self.leading_value = leading_value
        self.link_value = link_value
        self.trailing_address = trailing_address

    


link_1 = Link(6, 10, 2)
print("Leading value:" + str(link_1.leading_value) + " Link value:" + str(link_1.link_value) + " Leading value:" + str(link_1.trailing_address))

