class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f"{self.head}"

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


my_lst = LinkedList()

my_lst.append(1)
my_lst.append(2)
my_lst.append(3)

print(my_lst)