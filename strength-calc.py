# Strength calculator - each lift vs bodyweight

bodyweight = float(input("Your bodyweight (kg): "))
squat = float(input("Your squat (kg): "))
bench = float(input("Your bench press (kg): "))
deadlift = float(input("Your deadlift (kg): "))

squat_ratio = squat / bodyweight
bench_ratio = bench / bodyweight
deadlift_ratio = deadlift / bodyweight

print(f"\nSquat: {squat_ratio:.2f}x bodyweight")
if squat_ratio < 1:
    print("  Level: Beginner")
elif squat_ratio < 1.5:
    print("  Level: Novice")
elif squat_ratio < 2:
    print("  Level: Intermediate")
else:
    print("  Level: Advanced")

print(f"\nBench: {bench_ratio:.2f}x bodyweight")
if bench_ratio < 0.75:
    print("  Level: Beginner")
elif bench_ratio < 1:
    print("  Level: Novice")
elif bench_ratio < 1.5:
    print("  Level: Intermediate")
else:
    print("  Level: Advanced")

print(f"\nDeadlift: {deadlift_ratio:.2f}x bodyweight")
if deadlift_ratio < 1.25:
    print("  Level: Beginner")
elif deadlift_ratio < 1.75:
    print("  Level: Novice")
elif deadlift_ratio < 2.5:
    print("  Level: Intermediate")
else:
    print("  Level: Advanced")