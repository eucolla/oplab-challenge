# Linked list

class Node:  # Create Node Class
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:  # Create Linked list Class
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def traverse(self):
        if self.head is None:
            print("Linked Lista is empty!")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item, "")
                temp = temp.ref

    def delete(self, d_node):
        temp = self.head
        if self.head.item == d_node:
            self.head = self.head.ref
            return
        while temp is not None:
            if temp.ref.item == d_node:
                break
            temp = temp.ref

        if temp.ref is None:
            print("Item not found")
        else:
            temp.ref = temp.ref.ref


new_l = LinkedList()

new_l.insert_at_start(5)
new_l.insert_at_start(4)
new_l.insert_at_start(3)
new_l.insert_at_start(2)
new_l.insert_at_start(1)

new_l.traverse()

num_del = int(input(f'Enter the value for delete: '))

new_l.delete(num_del)
new_l.traverse()
