"""CCIT4020 Introduction to Computer Programming
HKU SPACE Community College
laboratory 4a"""

#Section 1: IF-Loops
print("CCIT4020 Laboratory 4: Section 1\n")

print("Enter two number for comparisons:")
first = float(input("    Enter the first float number: "))
second = float(input("    Enter the second float number: "))
print(f"The entered numbers are {first} and {second}")
first = round(first, 2)
second = round(second, 2)
if first > second:
    print(f"    It appears that {first} larger than {second} by {first - second}")
elif first == second:
    print(f"    It appears that {first} equals {second}")
elif first < second:
    print(f"    It appears that {first} smaller than {second} {second - first}")
else:
    print("Error, please input again")

print("\nCompleted by Song Man Tsun ...CCIT4020 ICP...")
