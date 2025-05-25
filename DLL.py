rom operator import truediv


class Node:
    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None


def Create_DLL(list):
    while True:
        x = int(input("Enet data value"))
        list.data = x
        ans = input("create next node Y or y or N or n")
        if ans == "N" or ans == "n":
            list.next = None
            break
        list.next = Node()
        list.next.prev = list
        list = list.next
def insert_at_first(list):
    h = list
    x = int(input("Enter first node data value"))
    new_node = Node()
    new_node.data = x
    new_node.next = list
    list.prev = new_node
    return new_node

def find_node(list,value):
    while True:
        if list.data == value:
            return list
        return None

def insert_at_specific(list):
    x = int(input("Enter data value you add"))
    search = int(input("insert aster which node"))
    abc = find_node(list,search)
    if abc != None:
        new_node = Node()
        new_node.data = x
        new_node.next = abc.next
        abc.next.prev = new_node
        new_node.prev = abc
        abc.next = new_node

def insert_after_last(list):
    x = int(input("Enter a the value addd"))
    n1 = Node()
    n1.data = x
    while True :
        if list.next.next == None :
            list.next = n1
            n1.prev = list.next
        list = list.next


def first_node(list):
    temp = list
    head  = list.next
    del temp
    return head

def find_node1(list,data):
    while True:
        if list.next.data == data:
            return list
        return None
def specific_Node(list):
    x = int(input("which node you delete "))
    n1 = find_node1(list,data)
    if n1 != None:
        temp = n1.next
        n1.nnext = n1.next.next
        del temp
        return list






def display(list):
    while True:
        print(list.data,"-",">")
        list = list.next
head = Node()

abc = Create_DLL(head)
display(abc)
por = insert_at_first(abc)
display(por)


