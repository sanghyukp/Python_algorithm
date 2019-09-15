# main.py
import pdb

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_A.next = node_B
    node_B.next = node_C
    node_B.prev = node_A
    node_C.next = node_D
    node_C.prev = node_B
    node_D.prev = node_C

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    #pdb.set_trace()
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
    
    new_node.next = node_T
    new_node.prev = node_P
    node_P.next = new_node
    node_T.prev = new_node

def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    next_next_node = next_node.next

    if pre_node.data == del_data:
        node1 = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            next_next_node = next_node.next
            pre_node.next = next_node.next
            #pdb.set_trace()            
            next_next_node.prev = next_node.prev
            del next_node
            break
        next_node = next_node.next


if __name__ == '__main__':
    print("연결 리스트 초기화")
    init_list()
    insert_node("B")
    print_list()
    print("노드 D의 삭제후")
    delete_node("C")
    print_list()
    