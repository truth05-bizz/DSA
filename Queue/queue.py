class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def dequeue(self):
        if not self.head:
            return None

        removed_data = self.head.data

        if not self.head.next:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_data

        self.head = self.head.next
        self.length -= 1
        return removed_data

    def peek(self):
        if not self.head:
            return None

        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length

    def show(self):
        if not self.head:
            return None

        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


ql = Queue()
ql.enqueue("Truth")
ql.enqueue("Ben")
ql.enqueue("Joy")

ql.show()
removed = ql.dequeue()
print(f"Removed Data: {removed}")
ql.show()
print()

ql.enqueue("Mark")
ql.enqueue("Hero")
ql.enqueue("Obia")

ql.show()
data_size = ql.size()
print(f"Data Size: {data_size}")
if not ql.is_empty():
    print(f"First Data: {ql.peek()}")

else:
    print("List is empty. ")
