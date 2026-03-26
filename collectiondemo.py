from collections import namedtuple

student1=namedtuple('student1',['name','rollno','marks'])
var=student1(name='sai',rollno=237,marks=89)
print('name',var.name)
print('rollno',var.rollno)
print('marks',var.marks)

from collections import deque

d=deque("xyz")
for i in d:
    print(i)
print(d)

from collections import ChainMap

d1={'one':1,'two':2}
d2={'three':3,'four':4}
c=ChainMap(d1,d2)
print(c)

from collections import Counter
list=['x','x','z','x','y','x','y','z']
print(Counter(list))

from collections import OrderedDict

od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
for key,value in od.items():
    print(key,":",value)

arr=[1,2,2,3,3,3,4]
freq=Counter(arr)
print(freq)
s='aabbbcc'
print(Counter(s))
print(freq.most_common(1))
from collections import defaultdict
d=defaultdict(int)
d["a"]+=1
print(d)

# edges = [(1,2), (1,3), (2,4)]

# graph = defaultdict(list)
# for u, v in edges:
#     graph[u].append(v)

# get(k,d) safe access
#  keys() all keys
#  values() all values
# items() key-values pairs
# update() merge dict
# pop(k) remove keys
# popitem() remove last item
# setdefault(k,v) insert if not exist
# clear() remove all 

d={"a":1,"b":2}
print(d.get('c',0))
d.setdefault("c",3)
print(d)
d.update({"d":4})
print(d)
# Counter Methods
from collections import Counter

c=Counter("aabbbcc")
print(c)
#  most_common(n) Top N elements
#  elements() Expand frequencies
#  update() add counts
#  subtract() subtract counts
#  clear()  removal all

from collections import defaultdict
d = defaultdict(int)
# 
# default_factory	Default value
# get()	Safe access
# items()	Pairs
# clear()	Reset

graph = defaultdict(list)
graph[1].append(2)
