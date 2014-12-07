# version code a3133383da20
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

import sys
import itertools
sys.path.insert(1,'util')
from GF2 import one



## 1: (Problem 2.14.1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [v + u for (v, u) in zip(p1_v, p1_u)]
p1_v_minus_u = [v - u for (v, u) in zip(p1_v, p1_u)]
p1_three_v_minus_two_u = [3*v - 2*u for (v, u) in zip(p1_v, p1_u)]


## 2: (Problem 2.14.2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [v + u for (v, u) in zip(p2_v, p2_u)]
p2_v_minus_u = [v - u for (v, u) in zip(p2_v, p2_u)]
p2_two_v_minus_u = [2*v - u for (v, u) in zip(p2_v, p2_u)]
p2_v_plus_two_u = [v + 2*u for (v, u) in zip(p2_v, p2_u)]



## 3: (Problem 2.14.3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3_v = [0,one,one]
p3_u = [one,one,one]
p3_vector_sum_1 = [v + u for (v, u) in zip(p3_v, p3_u)]
p3_vector_sum_2 = [v + u + u for (v, u) in zip(p3_v, p3_u)]



## 4: (Problem 2.14.4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.
veca = [one, one, 0, 0, 0, 0, 0]
vecb = [0, one, one, 0, 0, 0, 0]
vecc = [0, 0, one, one, 0, 0, 0]
vecd = [0, 0, 0, one, one, 0, 0]
vece = [0, 0, 0, 0, one, one, 0]
vecf = [0, 0, 0, 0, 0, one, one]
u1 = [0, 0, one, 0, 0, one, 0]
u2 = [0, one, 0, 0, 0, one, 0]

def add2(u, v):
    return [v + u for (v, u) in zip(v, u)]

def add3(u, v, x):
    return [v + u + x for (v, u, x) in zip(v, u, x)]

allvec = [veca, vecb, vecc, vecd, vece, vecf]

vdict = {}
vdict['bc'] = add2(vecb, vecc)
vdict['bd'] = add2(vecb, vecd)
vdict['be'] = add2(vecb, vece)
vdict['cd'] = add2(vecc, vecd)
vdict['ce'] = add2(vecc, vece)
vdict['de'] = add2(vecd, vece)
vdict['bcd'] = add3(vecb, vecc, vecd)
vdict['bce'] = add3(vecb, vecc, vece)
vdict['bde'] = add3(vecb, vecd, vece)
vdict['cde'] = add3(vecc, vecd, vece)
vdict['bcde'] = add2(add3(vecb, vecc, vecd), vece)

for i in vdict.keys():
    if vdict[i] == u1:
        print(i, " == u1")
        u_0010010 = i
    if vdict[i] == u2:
        print(i, " == u2")
        u_0100010 = i

u_0010010 = ('c', 'd', 'e')
u_0100010 = ('b', 'c', 'd', 'e')
u_0010010 = {'c', 'd', 'e'}
u_0100010 = {'b', 'c', 'd', 'e'}

# {'a','b','c'} is the subset consisting of:


## 5: (Problem 2.14.5) GF2 Vector Addition B
# Use the same format as the previous problem

labels = ['a', 'b', 'c', 'd', 'e', 'f']
allv = {'a':[one, one, one, 0, 0, 0, 0],
        'b':[0, one, one, one, 0, 0, 0],
        'c':[0, 0, one, one, one, 0, 0],
        'd':[0, 0, 0, one, one, one, 0],
        'e':[0, 0, 0, 0, one, one, one],
        'f':[0, 0, 0, 0, 0, one, one] }
u1 = [0, 0, one, 0, 0, one, 0]
u2 = [0, one, 0, 0, 0, one, 0]
u1 = [0, 0, one, 0, 0, 0, 0]

v_0010010 = []
v_0100010 = []
for L in range(0, len(labels)+1):
    for subset in itertools.combinations(labels, L):
        if len(subset) > 1:
            base = allv[subset[0]]
            for K in range(1,len(subset)):
                base = add2(base, allv[subset[K]])
            if base == u1:
                v_0010010.append(''.join(subset))
                # v_0010010.append(''.join(subset))
            if base == u2:
                v_0100010.append(''.join(subset))
                # v_0100010.append(''.join(subset))

v_0010010 = {'c', 'd'}
v_0100010 = set()
print(v_0010010) # "cd"
print(v_0100010) # no match


## 6: (Problem 2.14.6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.
x_gf2 = [0, 1, 1, 1]



## 7: (Problem 2.14.7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
def list_dot(u, v):
    return sum([a*b for (a,b) in zip(u,v)])

v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

x1 = [1,1,-1,1]
x2 = [8, -4, 1, 8]
x3 = [1, 6, 1, 1]
print("10 =", list_dot(x1, v1))
print("35 =", list_dot(x2, v2))
print("8 =", list_dot(x3, v3))


## 8: (Problem 2.14.9) Practice with Dot-Product
uv_a = list_dot([1,0], [5,4321])
uv_b = list_dot([0,1], [12345,6])
uv_c = list_dot([-1,3], [5,7])
uv_d = list_dot([-0.7071, 0.7071], [0.7071, -0.7071]) # or -1
uv_d = -1

