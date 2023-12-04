##************************ Solution to Question 1 ************************
sample = [2, 4, 4, 4, 5, 5, 7, 9]

def length_func(b):
    count = 0
    for _ in sample:
        count += 1
    return count

def mean_x(c):
    sum = 0
    for i in sample:
        sum += i
    xb = sum/length_func(sample)
    return xb

def sumsq(d):
    m = 0
    for i in sample:
        m += (i - mean_x(sample)) ** 2
    return m

def sqrt(e):
    num = 1
    while num * num <= e:
        num += 1
    return num - 1


h = sumsq(sample)/(length_func(sample) - 1)

print(f"Answer of first question: {sqrt(h)}")



#************************ Solution to Question 2 ************************


# Code for getting output 1.
input1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
two_d_list = []

a= []
for i in input1[0]:
    x = i % 10
    a.append(x)
two_d_list.append(a)

b = []
for j in input1[1]:
    y = j % 10
    b.append(y)
two_d_list.append(b) 

c = []
for k in input1[2]:
    z = k % 10
    c.append(z)  
two_d_list.append(c)

d = []
for l in input1[3]:
    m = l % 10
    d.append(m)  
two_d_list.append(d)


print(two_d_list)



# Code for getting output 2.
odd_even_two_d_list = []

oe1 = []
for i in input1[0]:
    if i % 2 == 0:
        oe1.append("Even")
    else:
        oe1.append("Odd")
odd_even_two_d_list.append(oe1)

oe2 = []
for i in input1[1]:
    if i % 2 == 0:
        oe2.append("Even")
    else:
        oe2.append("Odd")
odd_even_two_d_list.append(oe2)

oe3 = []
for i in input1[2]:
    if i % 2 == 0:
        oe3.append("Even")
    else:
        oe3.append("Odd")
odd_even_two_d_list.append(oe3)

oe4 = []
for i in input1[3]:
    if i % 2 == 0:
        oe4.append("Even")
    else:
        oe4.append("Odd")
odd_even_two_d_list.append(oe4)

print(odd_even_two_d_list)


# Code for getting output 3.
output3_list = []
for i in two_d_list:
    sum = 0
    for j in i:
        sum += j
    output3_list.append(sum)    
print(output3_list)

# Code for getting output 4.
output4_list = []
for i in output3_list:
    if i % 2 == 0:
        output4_list.append("Even")
print(output4_list)
