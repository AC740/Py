
# linked list

# get_size()
# find()
# add(data)
# remove(data)

class node(object):
    def __init__(self, data, nextNode = None):
        self.nextNode = nextNode
        self.data = data
    def getNext(self):
        return self.nextNode
    def setNext(self, lnode = None):
        self.nextNode = lnode
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

class linkedlist:
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    def getSize(self):
        return self.size
    def add(self, data):
        new_node = node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.getNext()
            return False
        
    
llist = linkedlist()
print("%".format(i for i in llist))
