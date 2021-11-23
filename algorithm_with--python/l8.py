from queue import Queue
from typing import Counter
def radix_sort(A):
    queus =[]
    for i in range(BUCKETS) :
        queus.append(Queue())
    
    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) :
            queus[(A[i]//factor) % 10].put(A[i])
        j = 0
        for b in range(BUCKETS) :
            while not queus[b].empty() :
                A[j] = queus[b].get()
                j +=1
        factor *= 10
        print("step", d+1, A)


import random
BUCKETS = 10
DIGITS = 4
data = []
for i in range(10) :
    data.append(random.randint(1,9999))
radix_sort(data)
print("Radix:", data)

NO_OF_CHARS = 128
def shift_table(pat) :
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    return tbl

def search_horspool(T, P) :
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while(i <= n-1) :
        k = 0
        while k <= m-1 and P[m-1-k]==T[i-k] :
            k += 1
        if k == m :
            return i-m+1
        else :
            print(T[i])
            print(t[ord(T[i])])
            i += t[ord(T[i])]
            print(i)
    return -1

print("퍼턴의 위치 :", search_horspool("APPLEMANGOBANANAGGRAPE", "BANANA"))


M = 13
table = [None]*M
def hashFn(key) :
    return key % M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
        id = (id + 1 + M) % M
        count -= 1
    if count < 0 :
        table[id] = key
    return

def lp_search(key) :
    id = hashFn(key)
    count = M
    while count>0:
        if table[id] == None :
            return None
        
        if table[id] != -1 and table[id] == key :
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    return None

def lp_delete(key) :
    id = hashFn(key)
    count = M
    while count>0:
        if table[id] == None : return
        if table[id] != -1 and table[id] == key :
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

print("  죄초:", table)
lp_insert(45); print( "45 삽입:", table)
lp_insert(27); print( "45 삽입:", table)
lp_insert(88); print( "45 삽입:", table)
lp_insert(8); print( "45 삽입:", table)
lp_insert(71); print( "45 삽입:", table)
lp_insert(60); print( "45 삽입:", table)
lp_insert(46); print( "45 삽입:", table)
lp_insert(38); print( "45 삽입:", table)
lp_insert(45); print( "45 삽입:", table)
lp_insert(45); print( "45 삽입:", table)