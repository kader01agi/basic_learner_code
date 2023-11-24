
#************************** Assignment 05 ***************************************
# Title: Sum of ASCII value of strings from a list.


generated_list = []

given_list = ["abc", "def", "ghi", "jkl"]
for i in given_list:
    sum = 0
    for j in i:
        sum = sum + ord(j)
    generated_list.append(sum)

print(generated_list)
