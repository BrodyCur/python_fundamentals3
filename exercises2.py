grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

def output_list(list):
    for item in list:
        print(f"* {item}")
    print(len(list))
    if item in list == "bananas":
        print("You need to pick up bananas.")
    else:
        print("You don't need bananas today.")

grocery_list.append('rice')

output_list(grocery_list)