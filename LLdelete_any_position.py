class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def apppend(self,data):
        new_node = Node(data)
        if  self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        return self.head
    
    def print_list(self,head):
        curr = head
        while curr != None:
            print(curr.data, end=" ->")
            curr = curr.next
        print("None")


    def insert_after_this_value(self,value):
        if self.head == None:
            print("Empty list")
            return 0
        else:
            curr = self.head
            xyz = int(input("Enter new node value"))
            new_node = Node(xyz)
            while curr.data != value and curr.next != None:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        return self.head
    
#########################################################################
    def delete_any_position(self,value):
        if self.head == None:
            return None
        else:
            curr = self.head
            while curr.next != None and curr.next.data != value:
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            del temp
            return self.head





# Example usage


abc =  LinkedList()
abc.apppend(1)
abc.apppend(2)
abc.apppend(3)
abc.apppend(4)
abc.apppend(5)
abc.print_list(abc.head)
abc.insert_after_this_value(3)
abc.print_list(abc.head)
abc.delete_any_position(34)
abc.print_list(abc.head)

