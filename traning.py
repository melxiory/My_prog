import sys

n = int(sys.stdin.readline())
list_comm = [[int(i) if i.isdigit() else i for i in sys.stdin.readline().strip().split()] for _ in range(n)]


class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key
        self.sum = 0


def set_parent(child, parent):
    if child != None:
        child.parent = parent


def keep_parent(v):
    set_parent(v.left, v)
    set_parent(v.right, v)


def rotate(parent, child):
    gparent = parent.parent
    if gparent != None:
        if gparent.left == parent:
            gparent.left = child
        else:
            gparent.right = child
    child.sum = parent.sum
    if parent.left == child:
        parent.left, child.right = child.right, parent
        if child.left != None:
            parent.sum = child.sum - child.left.sum - child.key
        else:
            parent.sum = child.sum - child.key
    else:
        parent.right, child.left = child.left, parent
        if child.right != None:
            parent.sum = child.sum - child.right.sum - child.key
        else:
            parent.sum = child.sum - child.key

    keep_parent(child)
    keep_parent(parent)
    child.parent = gparent


def splay(v):
    if v.parent == None:
        return v
    parent = v.parent
    gparent = parent.parent
    while True:
        if gparent == None:
            rotate(parent, v)
            break
        zigzig = (gparent.left == parent) == (parent.left == v)
        if zigzig:
            rotate(gparent, parent)
            rotate(parent, v)
        else:
            rotate(parent, v)
            rotate(gparent, v)
        parent = v.parent
        if parent == None:
            break
        gparent = parent.parent
    return v

def find(v, key):
    if v == None:
        return None
    while True:
        if key == v.key:
            break
        if key < v.key and v.left != None:
            v = v.left
            continue
        if key > v.key and v.right != None:
            v = v.right
            continue
        break
    return splay(v)

def split(root, key):
    if root == None:
        return None, None
    if root.key < key:
        right, root.right = root.right, None
        set_parent(right, None)
        if right != None:
            root.sum = root.sum - right.sum
        return root, right
    else:
        left, root.left = root.left, None
        set_parent(left, None)
        if left != None:
            root.sum = root.sum - left.sum
        return left, root


def insert(root, key):
    left, right = split(root, key)
    root = Node(key, left, right)
    if left != None and right != None:
        root.sum = left.sum + right.sum + key
    elif left != None:
        root.sum = left.sum + key
    else:
        root.sum = right.sum + key
    keep_parent(root)
    return root


def remove(root, key):
    set_parent(root.left, None)
    set_parent(root.right, None)
    if root.right == None:
        return root.left
    if root.left == None:
        return root.right
    root.right = find(root.right, root.left.key)
    root.right.left, root.left.parent = root.left, root.right
    if root.right.left != None and root.right.right != None:
        root.right.sum = root.right.left.sum + root.right.right.sum + root.right.key
    elif root.right.left != None:
        root.right.sum = root.right.left.sum + root.right.key
    else:
        root.right.sum = root.right.right.sum + root.right.key
    return root.right

def summ(v, l, r):
    if v == None:
        return 0, v
    if v.sum == 0:
        return 0, v
    v = find(v, l)
    acc = v.sum
    if l > v.key:
        if v.left != None:
            acc -= (v.left.sum + v.key)
        else:
            acc -= v.key
    elif l <= v.key <= r:
        if v.left != None:
            acc -= v.left.sum
    else:
        return 0, v
    v = find(v, r)
    if r < v.key:
        if v.right != None:
            acc -= (v.right.sum + v.key)
        else:
            acc -= v.key
    elif l <= v.key <= r:
        if v.right != None:
           acc -= v.right.sum
    else:
        return 0, v
    return acc, v

v_key = None
s = 0
for i in list_comm:
    if i[0] == 's':
        f_l = (i[1] + s) % 1000000001
        f_r = (i[2] + s) % 1000000001
        s, v_key = summ(v_key, f_l, f_r)
        print(s)
        continue
    f_i = (i[1] + s) % 1000000001
    if i[0] == '+':
        if v_key == None:
            v_key = Node(f_i)
            v_key.sum = v_key.key
            continue
        v_key = find(v_key, f_i)
        if v_key.key == f_i:
            continue
        v_key = insert(v_key, f_i)
        continue
    if i[0] == '-':
        if v_key == None:
            continue
        v_key = find(v_key, f_i)
        if v_key.key == f_i:
            v_key = remove(v_key, f_i)
        continue
    if i[0] == '?':
        if v_key:
            v_key = find(v_key, f_i)
            if v_key.key == f_i:
                print('Found')
            else:
                print('Not found')
        else:
            print('Not found')

'''
    if v == None:
        return 0
    if l <= v.key <= r:
        return v.key + summ(v.left, l, r) + summ(v.right, l, r)
    if v.key > r:
        return summ(v.left, l, r)
    if v.key < l:
        return summ(v.right, l, r)
    
    
    def merge(left, right):
    if right == None:
        return left
    if left == None:
        return right
    right = find(right, left.key)
    right.left, left.parent = left, right
    return right
    
    
        if v.parent == None:
        return v
    parent = v.parent
    gparent = parent.parent
    if gparent == None:
        rotate(parent, v)
        return v
    else:
        zigzig = (gparent.left == parent) == (parent.left == v)
        if zigzig:
            rotate(gparent, parent)
            rotate(parent, v)
        else:
            rotate(parent, v)
            rotate(gparent, v)
        return splay(v)
        
        
       if v == None:
        return None
    if key == v.key:
        return splay(v)
    if key < v.key and v.left != None:
        return find(v.left, key)
    if key > v.key and v.right != None:
        return find(v.right, key)
    return splay(v)     
'''