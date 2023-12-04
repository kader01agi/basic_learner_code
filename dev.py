# input1 = int(input("what is input1? "))

# # output 1
# output1 = input1 % 10
# print(output1)


# # output 2
# if input1 % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # output 3
# output3 = []
# if input1 % 2 == 0:
#     output3.append(input1)
#     print(output3)
# else:
#     print("Odd")

# # output 4



# sample = [2, 4, 4, 4, 5, 5, 7, 9]
# def my_sqrt(x):
#   if x < 0:
#     raise ValueError("Cannot calculate square root of a negative number")
#   elif x == 0:
#     return 0
#   else:
#     guess = 1
#     while guess * guess <= x:
#       guess += 1
#     return guess - 1
  

def my_sqrt(e):
#   if x < 0:
#     raise ValueError("Cannot calculate square root of a negative number")
#   elif x == 0:
#     return 0
#   else:
    num = 1
    while num * num <= e:
        num += 1
    return num - 1

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
