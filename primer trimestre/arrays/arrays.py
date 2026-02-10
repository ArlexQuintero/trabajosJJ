# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()


# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         s += a[i][j]
# print(s)

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# s = 0
# for row in a:
#     for elem in row:
#         s += elem
# print(s)

# n = int(input(3)) 
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split()])

# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
#         else:
#             a[i][j] = 1
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# n = 4
# a = [0] * n
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# matriz=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# print (matriz)
# matriz.remove([6,7,8,9,10])
# print(matriz)
# matriz.insert(2,[16,17,18,19,20])
# print(matriz)
# matriz.pop(0)
# print(matriz)

matriz=[[3,4,9,9,5],[6,5,6,7,7],[6,1,4,7,4],[5,9,2,3,1],[8,4,6,2,0]]
# print ({matriz[0][4]})
# print (matriz[2][3])
# print (matriz[4][0])
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()

print("--- a mano ---")
print (f"""
{matriz[0][0]} * * * *
* {matriz[1][1]} * * *
* * {matriz[2][2]} * *
* * * {matriz[3][3]} *
* * * * {matriz[4][4]}
    """)
print("---con siclos ---")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i ==j:
            print(matriz[i][j],end=' ')
        else:
            print('*',end=' ')
    print()
print("--- con siclos 2 ---")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i + j == len(matriz) -1:
            print(matriz[i][j],end=' ')
        else:
            print('*',end=' ')
    print()