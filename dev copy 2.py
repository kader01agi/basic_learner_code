
#************************ Solution to Question 1 ************************
sample = [2, 4, 4, 4, 5, 5, 7, 9]

def leng(b):
    count = 0
    for _ in sample:
        count += 1
    return count

def xbar(c):
    sum = 0
    for i in sample:
        sum += i
    xb = sum/leng(sample)
    return xb

def sumsq(d):
    m = 0
    for i in sample:
        m += (i - xbar(sample)) ** 2
    return m

def sqrt(e):
    num = 1
    while num * num <= e:
        num += 1
    return num - 1


h = sumsq(sample)/(leng(sample) - 1)

# print(sqrt(h))



#************************ Solution to Question 2 ************************

input1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# output 1
output1 = []
for i in input1:
    for j in i:
        x = j % 10
        output1.append(x)
# print(output1)

# Another approach to output 1
for i in input1:
    for j in i:
        x = j % 10
        print(x, end=" ")
    print()


# output 2
for i in input1:
    for j in i:
        if j % 2 == 0:
            print("Even", end=" ")
        else:
            print("Odd", end=" ")
    print()
