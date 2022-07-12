# With a node given as input, remove the node from list

def delete(node):
    node.val = node.next.val
    node.next = node.next.next