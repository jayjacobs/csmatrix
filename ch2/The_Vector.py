# version code 0d1e4db3d840
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one

def add2(v, w):
    return [v[0]+w[0], v[1]+w[1]]

def minus2(v, w):
    return [v[0]-w[0], v[1]-w[1]]

def scalar_vector_mult(alpha, v):
    return [ alpha*v[i] for i in range(len(v)) ]

def list_dot(u, v):
    return sum([a*b for (a,b) in zip(u,v)])

## 1: (Problem 2.14.1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = add2(p1_v, p1_u)
p1_v_minus_u = minus2(p1_v, p1_u)
p1_three_v_minus_two_u = minus2(scalar_vector_mult(3, p1_v), scalar_vector_mult(3, p1_u))


def add(v,w):
    return [ a+b for (a,b) in zip(v,w) ]

def minus(v,w):
    return [ a-b for (a,b) in zip(v,w) ]

## 2: (Problem 2.14.2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = add(p2_v, p2_u)
p2_v_minus_u = minus(p2_v, p2_u)
p2_two_v_minus_u = minus(scalar_vector_mult(2, p2_v), p2_u)
p2_v_plus_two_u = add(p2_v, scalar_vector_mult(2, p2_u))



## 3: (Problem 2.14.3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3v = [0, one, one]
p3u = [one, one, one]
p3_vector_sum_1 = add(p3v, p3u)
p3_vector_sum_2 = add(p3v, add(p3u,p3u))



## 4: (Problem 2.14.4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.

u_0010010 = ...
u_0100010 = ...



## 5: (Problem 2.14.5) GF2 Vector Addition B
# Use the same format as the previous problem

v_0010010 = ...
v_0100010 = ...



## 6: (Problem 2.14.6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.
x_gf2 = [...]



## 7: (Problem 2.14.7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
v1 = [...]
v2 = [...]
v3 = [...]



## 8: (Problem 2.14.9) Practice with Dot-Product
uv_a = ...
uv_b = ...
uv_c = ...
uv_d = ...

