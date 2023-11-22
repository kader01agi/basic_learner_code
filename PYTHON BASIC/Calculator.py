# Unpopular mundane method
x = input("What is x? ")
y = input("What is y? ")
z = int(x) + int(y)
print(z)

# TALENTED METHOD
x = int(input("What is x? "))
y = int(input("What is y? "))
print(x + y)

# COMPLICATED UGLY Coding
print(int(input("What is x? ")) + int(input("What is y? ")))


# TALENTED METHOD
x = float(input("What is x? "))
y = float(input("What is y? "))
z = round(x + y)            # Rounds a number.
print(z)
z = round(x + y, 2)         # Rounds decimal to 2 digit.

# prints 2 digit after decimal.
z = (x / y)
print(f"{z:.2f}")

# Add a comma before a thousand
print(f"{z:,}")




# Rounds decimal to 2 digit.
z = round(x / y, 2)
print(z)

# GRADE Calculator Mundane/Boring
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print ("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print ("Grade: D")
else:
    print ("Grade: F")

# GRADE Calculator Dull/Boring
score = int(input("Score: "))
if 90 <= score <= 100:
    print ("Grade: A")
elif 80<= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print ("Grade: D")
else:
    print ("Grade: F")

# GRADE Calculator TALLENTED
score = int(input("Score: "))
if score >= 90:
    print ("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print ("Grade: C")
elif score >= 60:
    print ("Grade: D")
else:
    print ("Grade: F")