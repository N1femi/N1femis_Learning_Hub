# Terminology

**Abstract Data Type**: The logical description of how one views data without regard to how it will eventually be implemented

**Data Structure**: Is the impkementation of an *abstract data type*, it is also a way of storing and organizing data for efficient operations

**Node**: Foundation of some Data Structures(Linked Lists, Trees) are implemented as shown:
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```
On top of having a value like any other variable, Nodes have `self.next` which acts as a pointer to the next node.

**Linear Data Structures**: Data Structures whose items are ordered depending on how they are added ad removed. *think of it as one straight path* Examples: Queues, Stacks, Linked Lists. Note: What differentiates Linear data structures are how their items are added & removed.

