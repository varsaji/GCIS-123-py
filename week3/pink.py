age = int(input("please enter your age: "))
if age < 1:
    print("infant")
elif age < 4:
    print("toddler")
elif age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult")
else:
    print("senior citizen")