class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert(self, data, new_data):
        new_node = Node(new_data)

        if not self.head:
            self.head = new_node
            return

        curr = self.head

        while curr and curr.data != data:
            curr = curr.next

        if curr is None:
            print("Item not found")
            return

        new_node.next = curr.next
        curr.next = new_node

    def delete(self, data):

        if not self.head:
            print("List is empty. ")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head

        while curr:
            if curr.data == data:
                prv_curr.next = curr.next

                print(f"'{data}' deleted successfully. ")
                break

            prv_curr = curr

            curr = curr.next

        else:
            print(f"No data '{data}' found")

    def search(self, data):

        if not self.head:
            print("List is empty.")
            return

        curr = self.head

        while curr:
            if curr.data == data:
                print("Item found")
                break

            curr = curr.next

        else:
            print("No item in list")

    def length(self):
        curr = self.head
        count = 0

        while curr:
            curr = curr.next

            count += 1

        print(f"List Length: {count}")

    def display(self):
        curr = self.head

        while curr:
            print(f"{curr.data}")
            curr = curr.next


ll = Linkedlist()
ll.append("Truth")
ll.append("Ben")
ll.append("Mary")
ll.append("Joy")
ll.append("Mark")

ll.prepend("Serah")
ll.insert("Ben", "Hero")

ll.length()
ll.delete("Serah")

ll.search("Mark")
ll.display()
ll.length()
