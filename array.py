import sys

# Accept scores from command-line arguments
if len(sys.argv) > 1:
    scores = list(map(float, sys.argv[1:]))
else:
    scores = list(map(float, input("Enter scores separated by spaces: ").split()))

if len(scores) == 0:
    print("Please enter at least one score.")
else:
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)

    print("\nGrades:")
    for score in scores:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"{score}: {grade}")