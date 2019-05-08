

def grade(percentage):
    if percentage == 100 or percentage >= 95:
        return 'A'
    elif percentage == 94 or percentage >= 87:
        return 'A'
    elif percentage == 86 or percentage >= 80:
        return 'A-'
    elif percentage == 79 or percentage >= 77:
        return 'B+'
    elif percentage == 76 or percentage >= 73:
        return 'B'
    elif percentage == 72 or percentage >= 70:
        return 'B-'
    elif percentage == 69 or percentage >= 67:
        return 'C+'
    elif percentage == 66 or percentage >= 63:
        return 'C'
    elif percentage == 62 or percentage >= 60:
        return 'C-'
    elif percentage == 59 or percentage >= 57:
        return 'D+'
    elif percentage == 56 or percentage >= 53:
        return 'D'
    elif percentage == 52 or percentage >= 50:
        return 'D-'
    else:
        return 'R'

grade_in_percent = int(input("enter your percentage: "))

print(f"Your grade is: {grade(grade_in_percent)}")
