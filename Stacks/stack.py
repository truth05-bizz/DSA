class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.items:
            return "Empty list"

        remove_data = self.items.pop()
        return remove_data

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            return "Empty list"

        return self.items[-1]


ss = Stack()
ss.push(10)
ss.push(20)
# ss.push(30)
# ss.push(40)
# ss.push(50)
print(ss.peek())
print(ss.size())
if ss.is_empty():
    print("Empty")

else:
    print("Data in list")
data_removed = ss.pop()
print(f"removed: {data_removed}")
print(ss.size())
print(ss.peek())
