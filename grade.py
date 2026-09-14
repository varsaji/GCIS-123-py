percentage = float(input("Please enter your percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Must be between 0 and 100.")
elif percentage < 60:
    print("You got an F (Fail)")
elif percentage < 70:
    print("You got a D (Minimal Pass)")
elif percentage < 73:
    print("You got a C- (Satisfactory)")
elif percentage < 77:
    print("You got a C (Satisfactory)")
elif percentage < 80:
    print("You got a C+ (Satisfactory)")
elif percentage < 83:
    print("You got a B- (Good)")
elif percentage < 87:
    print("You got a B (Good)")
elif percentage < 90:
    print("You got a B+ (Good)")
elif percentage < 94:
    print("You got an A- (Excellent)")
else:
    print("You got an A (Excellent)")