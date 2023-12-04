# input1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# output1 = []
# for i in input1[0]:
#     for j in i:
#         x = j % 10
#         output1.append(x)
# print(output1)

# m = []
# n = []
# o = []
# p = []
# Q = []
# input1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# for i in input1[0]:
#     x = i % 10 
#     m.append(x)
# print(m)

# for j in input1[1]:
#     x = j % 10 
#     n.append(x)
# print(n)


# m.append(n)
# print(m)

input1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in input1:
    for j in i:
        x = j % 10
        print(x, end=" ")
    print()

