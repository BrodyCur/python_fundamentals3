def grade(percentage):
    if percentage <= 100 and percentage >= 95:
        return 'A'
    elif percentage <= 94 and percentage >= 87:
        return 'A'
    elif percentage <= 86 and percentage >= 80:
        return 'A-'
    elif percentage <= 79 and percentage >= 77:
        return 'B+'
    elif percentage <= 76 and percentage >= 73:
        return 'B'
    elif percentage <= 72 and percentage >= 70:
        return 'B-'
    elif percentage <= 69 and percentage >= 67:
        return 'C+'
    elif percentage <= 66 and percentage >= 63:
        return 'C'
    elif percentage <= 62 and percentage >= 60:
        return 'C-'
    elif percentage <= 59 and percentage >= 57:
        return 'D+'
    elif percentage <= 56 and percentage >= 53:
        return 'D'
    elif percentage <= 52 and percentage >= 50:
        return 'D-'
    elif percentage <= 49:
        return 'R'
    else:
        return 'Invalid Input!'

grade_in_percent = int(input("enter your percentage: "))

print(f"Your grade is: {grade(grade_in_percent)}")
