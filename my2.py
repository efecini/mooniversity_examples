"""
_ = set(map(int, input().split()))
arr = input().split()
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))

print(s1)
print(s2)
print(s3)
print(sum([(i in s1)-(i in s2) for i in arr]))

n, m = raw_input().split()

sc_ar = raw_input().split()

A = set(raw_input().split())
B = set(raw_input().split())
print sum([(i in A) - (i in B) for i in sc_ar])
"""
A = set(input().split())
B = set(input().split())
print(A)
print(B)
print(A.issuperset(B))