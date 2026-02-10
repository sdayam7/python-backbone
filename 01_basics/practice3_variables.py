#Goal: Use Modulus operator to check for even or odd numbers

number=37

#Calculate the remainder when divided by 2
remainder = number%2

print("Number:",number)
print("Remainder:",remainder)

if remainder ==0:
    print("This number is EVEN")
else:
    print("This number is ODD")

"""
LOGIC:
- Even numbers give remainder 0
- Odd numbers give remainder 1
- Modulus is heavily used in loops and indexing 

"""