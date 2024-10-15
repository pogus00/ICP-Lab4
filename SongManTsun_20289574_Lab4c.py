"""CCIT4020 Introduction to Computer Programming
HKU SPACE Community College
laboratory 4c"""

#Section 3: personal information
print("CCIT4020 Laboratory 4: Section 3\n")

marks = float(input("Please enter the numerical grade (out of 100):"))
if 0 <= marks < 45:
    print("The Letter Grade is F.")
elif 45 <= marks < 50:
    print("The Letter Grade is D.")
elif 50 <= marks < 55:
    print("The Letter Grade is C-.")
elif 55 <= marks < 60:
    print("The Letter Grade is C.")
elif 60 <= marks < 65:
    print("The Letter Grade is C+.")
elif 65 <= marks < 70:
    print("The Letter Grade is B-.")
elif 70 <= marks < 75:
    print("The Letter Grade is B.")
elif 75 <= marks < 80:
    print("The Letter Grade is B+.")
elif 80 <= marks < 85:
    print("The Letter Grade is A-.")
elif 85 <= marks < 90:
    print("The Letter Grade is A.")
elif 90 <= marks <= 100:
    print("The Letter Grade is A+.")
else:
    print("Error! Invalid input...")

print("\nCompleted by Song Man Tsun ...CCIT4020 ICP...")
