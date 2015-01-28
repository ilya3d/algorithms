# import sys
# n = int( input() )
# a = list(map(int, input().split()))
# m = int( input() )
# q = list(map(int, input().split()))
#
# for i in range( 1, n ):
#     a[i] = a[i-1] + a[i]
#
# b = list()
# for i in range(m):
#     z = q[i]
#     l1 = 0
#     l2 = n-1
#     while True:
#         ind = (l2 + l1) // 2
#         if z > a[ind]:
#             l1 = ind + 1
#         elif ind > 0 and z <= a[ind-1]:
#             l2 = ind
#         else:
#             ind += 1
#             b.append(str(ind))
#             break

def binary_search():
    #todo
    return True