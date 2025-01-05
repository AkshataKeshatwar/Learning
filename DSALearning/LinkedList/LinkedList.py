class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data)
        itr.next = node

    def print(self):
        itr = self.head
        result =[]
        while itr:
            result.append(str(itr.data))
            itr = itr.next         
        print("-->".join(result))

    

if __name__  == "__main__":
    LL = LinkedList()
    LL.insertAtBegining(10)
    LL.insertAtBegining(20)
    LL.insertAtBegining(50)
    LL.insertAtEnd(40)
    LL.print()
        