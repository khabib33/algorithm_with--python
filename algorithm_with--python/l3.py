
import queue

def topoLogical_sort2(graph) :
    inDeg = {}
    for v in graph :
        inDeg[v] = 0
    for v in graph :
        for u in graph[v]:
            inDeg[u] += 1
    vlist = queue.Queue()
    print(inDeg)
#    vlist = []
    for v in graph :
        if inDeg[v]==0:
            vlist.put(v)
    
    while not vlist.empty() :
        v = vlist.get()
        print(v, end=' ')

        for u in graph[v] :
            inDeg[u] -=1
            if inDeg[u]==0:
                vlist.put(u)

                
mygraph = { "A" : {"C", "D"},
            "B" : {"D", "E"},
            "C" : {"D", "F"},
            "D" : {"F"},
            "E" : {"F"},
            "F" : set()
}

print('topoLogical_sort2: ')
topoLogical_sort2(mygraph)
print()