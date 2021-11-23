class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def calc_height(root) :
    if root is None :
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft,hRight) + 1


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)
print("트리의 높이 =", calc_height(root))
print("-------------------------------------------------")


def preorder(n):
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('   In-Order :   ', end='')
inorder(root)
print()
print('   Pre-Order:   ', end='')
preorder(root)
print()
print('   Post-Order:  ', end='')
postorder(root)
print
print("-------------------------------------------------" )


def strip_closest(P, d) :
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1])

    for i in range(n) :
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min : 
            dij = dist(P[i], P[j])
            if dij < d_min :
                d_min = dij
            j += 1
    return d_min


import math
def distance(p1, p2) :
    n = len(P)
    mindist = float("inf")
    for i in range(n-1):
        for j in range(i+1, n) :
            dist = distance(P[i], P[j])
            if dist < mindist:
                mindist = dist
            return mindist
def strip_closest(P, d) :
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1])

    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min :
                d_min = dij
            return d_min
def closest_pair_dist(P, n) :
    if n <= 3 :
        return closest_pair_dist(P)
    
    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pair_dist(P[:mid], mid)
    dr - closest_pair_dist(P[mid:], n-mid)
    d = min(dl, dr)

    Pm = []
    for i in range(n) :
        if abs(P[i][0] - mid_x) < d :
            Pm.append(P[i])
    ds = strip_closest(Pm, d)
    return min(d, ds)

p = [(2,3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#p.sort(key = lambda point: point[0])
#print("가장 가까운 두 점의 거리", closest_pair_dist(p. len(p)))
p.sort(key = lambda k:k[0], reverse = True)
print(p)