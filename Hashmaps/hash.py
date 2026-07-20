class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.buckets = [None] * 10

    def get_index(self, key):
        total = 0

        for letter in key:
            total += ord(letter)

        return total % len(self.buckets)

    def put(self, key, value):
        index = self.get_index(key)
        new_node = Node(key, value)

        if self.buckets[index] is None:
            self.buckets[index] = new_node
            return

        curr = self.buckets[index]

        while curr:
            if curr.key == key:
                curr.value = value
                return

            if curr.next is None:
                break

            curr = curr.next

        curr.next = new_node

    def show(self, index):
        if self.buckets[index] is None:
            return None

        curr = self.buckets[index]

        while curr:
            print(f"{curr.key}: {curr.value}", end=" -> ")
            curr = curr.next

    def get(self, data):
        index = self.get_index(data)

        if self.buckets[index] is None:
            return None

        curr = self.buckets[index]

        while curr:
            if curr.key == data:
                return curr.value

            curr = curr.next

        return None

    def remove(self, data):
        index = self.get_index(data)

        if self.buckets[index] is None:
            return None

        if self.buckets[index].key == data:
            remove_value = self.buckets[index].value
            self.buckets[index] = self.buckets[index].next
            return remove_value

        curr = self.buckets[index]
        prv = None

        while curr:
            if curr.key == data:
                remove_value = curr.value
                prv.next = curr.next
                return

            prv = curr
            curr = curr.next

        return remove_value


hm = HashMap()
# hm.show()
"""
print(hm.get_index("Truth"))
print(hm.get_index("Ben"))
print(hm.get_index("Mary"))
print(hm.get_index("Joy"))
print(hm.get_index("John"))
print(hm.get_index("Martha"))
print(hm.get_index("Favour"))
print(hm.get_index("Maro"))
print(hm.get_index("Fidel"))
print(hm.get_index("Brown"))
print(hm.get_index("Emma"))
print(hm.get_index("Mosh"))
"""

hm.put("Truth", 81)
hm.put("Ben", 73)
hm.put("Mary", 67)
hm.put("Joy", 86)
hm.put("John", 91)
hm.put("Martha", 91)
hm.put("Favour", 50)
hm.put("Maro", 76)
hm.put("Fidel", 55)
hm.put("Brown", 96)
hm.put("Emma", 47)
hm.put("Mosh", 88)
print(hm.show(5))
print()
print(hm.get("Martha"))
print()
remove_data_value = hm.remove("Truth")
print(remove_data_value)
print(hm.show(5))
