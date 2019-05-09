grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

def output_list(list):
    for item in list:
        print(f"* {item}")
    print(len(list))
    if item in list == "bananas":
        print("You need to pick up bananas.")
    else:
        print("You don't need bananas today.")
    
    print(list[1])


grocery_list.append('rice')

output_list(grocery_list)

grocery_list.sort()

output_list(grocery_list)

grocery_list.remove('salmon')

output_list(grocery_list)