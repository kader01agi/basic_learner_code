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
td_list = []

a= []
for i in input1[0]:
    x = i % 10
    a.append(x)
td_list.append(a)

b = []
for j in input1[1]:
    y = j % 10
    b.append(y)
td_list.append(b) 

c = []
for k in input1[2]:
    z = k % 10
    c.append(z)  
td_list.append(c)

d = []
for l in input1[3]:
    m = l % 10
    d.append(m)  
td_list.append(d)


print(td_list)


for i in td_list:
    for j in i:
        if j % 2 == 0:
            print("Even", end=" ")
        else:
            print("Odd", end=" ")
    print()
