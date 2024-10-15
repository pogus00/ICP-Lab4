"""CCIT4020 Introduction to Computer Programming
HKU SPACE Community College
laboratory 4b"""

#Section 2: personal information
print("CCIT4020 Laboratory 4: Section 2\n")

print("Greetings! Please input some personal particulars...")
name = input("  What is your name?")
year = int(input("  In which year were you born?"))
gender = input("  What is your preferred gender? (m/f)")
print("The legal drinking age is 18! ")
year -= 2006
if year <= 0:
    if gender == 'm':
        print(f"Enjoy, Mr. {name} !")
    elif gender == 'f':
        print(f"Have a nice day and enjoy, Ms. {name}")
    else:
        print("Never mind. AI doesn't care about exceptions.")
elif year > 0:
    if gender == 'm':
        print(f"Oh boy, Mr. {name}, you are {year} years younger than the legal drinking age!...")
    elif gender == 'f':
        print(f"Oh girl, Ms. {name}, you are {year} years younger, be patient...")
    else:
        print("Never mind. AI doesn't care about exceptions.")

print("\nCompleted by Song Man Tsun ...CCIT4020 ICP...")
