class HashMap:
    def __init__(self):
        self.buckets = [None] * 10

    def get_index(self, key):
        total = 0

        for letter in key:
            total += ord(letter)

        return total % len(self.buckets)

    def put(self):
        pass

    def show(self):
        print(self.buckets)


hm = HashMap()
hm.show()
print(hm.get_index("Truth"))
print(hm.get_index("Ben"))
print(hm.get_index("Mary"))
