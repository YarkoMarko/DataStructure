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

    def delete(self, elem):
        if self.head is None:
            raise ValueError("List is empty")

        isInList = False
        check_elem = self.head

        while check_elem.data != elem:
            if check_elem.next is None:
                break

            check_elem = check_elem.next

        else:
            isInList = True

        if isInList:
            if self.head.data == elem:
                self.head = self.head.next
                return

            last_elem = self.head.next
            prev = self.head

            while last_elem.data != elem:
                prev = last_elem
                last_elem = last_elem.next

            prev.next = last_elem.next

            del last_elem

        else:
            raise ValueError(f"Can`t find {elem} in list")

    def check(self, data):
        if self.head is None:
            raise ValueError("List is empty")

        check_node = self.head

        isInList = False

        while check_node:
            if check_node.data == data:
                isInList = True
                break

            check_node = check_node.next

        if isInList:
            print(f"{data} is in list")

        else:
            print(f"{data} is not in list")

    def change(self, dataToChange):
        if self.head is None:
            raise ValueError("List is empty")

        check_node = self.head

        isInList = False

        while check_node:
            if check_node.data == dataToChange:
                isInList = True
                break

            check_node = check_node.next

        if isInList:
            new_data = int(input("Enter new data: "))

            check_node.data = new_data

        else:
            raise ValueError(f"Can`t find {dataToChange} in list")


my_lst = LinkedList()

print(my_lst)

while True:
    choice = int(input("Enter your choice (0 - break, 1 - add node, 2 - delete node, 3 - show elements, 4 - check element, 5 - change element: "))

    match choice:
        case 0:
            print("Goodbye!")
            break

        case 1:
            my_lst.append(int(input("Enter element: ")))

        case 2:
            my_lst.delete(int(input("Enter element: ")))

        case 3:
            print(my_lst)

        case 4:
            my_lst.check(int(input("Enter element: ")))

        case 5:
            my_lst.change(int(input("Enter element: ")))


