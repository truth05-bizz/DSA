class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        self.head = self.head.next

    def show(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


ql = Queue()
ql.enqueue(10)
ql.enqueue(20)
ql.enqueue(30)

ql.show()
print()
ql.dequeue()
ql.show()
