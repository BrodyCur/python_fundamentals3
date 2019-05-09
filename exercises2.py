# Exercise 9

# grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

# def output_list(list):
#     for item in list:
#         print(f"* {item}")
#     print(len(list))
#     if item in list == "bananas":
#         print("You need to pick up bananas.")
#     else:
#         print("You don't need bananas today.")
    
#     print(list[1])


# grocery_list.append('rice')

# output_list(grocery_list)

# grocery_list.sort()

# output_list(grocery_list)

# grocery_list.remove('salmon')

# output_list(grocery_list)


# Exercise 10

students = {
    "cohort1": 34,
    "cohort2": 42,
    "cohort3": 22
}

def display_cohorts(dict):
    for key, value in dict.items():
        value = value * 1.05
        print(f"{key}: {value:.0f}")
        

    print(dict.keys())

students['cohort4'] = 43

def cohort_calculator(dict):
    total = 0
    for key, value in dict.items():
        total += value

    print(total)

display_cohorts(students)
cohort_calculator(students)


students.pop('cohort2')


display_cohorts(students)
cohort_calculator(students)