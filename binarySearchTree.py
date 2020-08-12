class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

def binary_insert(root, node):
  if root is None:
    root = node
  else:
    if root.data > node.data:
      if root.left is None:
        root.left = node
      else:
        binary_insert(root.left, node)
    elif root.data < node.data:
      if root.right is None:
        root.right = node
      else:
        binary_insert(root.right, node)

def binary_search(root, data):
  if root.data == data:
    return root
  else:
    if root.data > data:
      binary_search(root.left, data)
    elif root.data < data:
      binary_search(root.right, data)

def in_order_visit(root, visit):
  if not root:
    return
  in_order_visit(root.left, visit)
  visit(root.data)
  in_order_visit(root.right, visit)

def pre_order_visit(root, visit):
  if not root:
    return
  visit(root.data)
  in_order_visit(root.left, visit)
  in_order_visit(root.right, visit)

def post_order_visit(root, visit):
  if not root:
    return
  in_order_visit(root.left, visit)
  in_order_visit(root.right, visit)
  visit(root.data)

def visit(data):
  print(data)

def pre(data):
  print(data * 2)

def post(data):
  print(data * 4)

def main():
  root = Node(7)
  binary_insert(root, Node(2))
  binary_insert(root, Node(5))
  binary_insert(root, Node(8))
  binary_insert(root, Node(12))
  print('---------------in----------------')
  in_order_visit(root, visit)
  print('---------------pre----------------')
  pre_order_visit(root, pre)
  print('---------------post----------------')
  post_order_visit(root, post)

if __name__ == "__main__":
    main()
