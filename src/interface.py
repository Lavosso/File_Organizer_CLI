def print_and_confirm_plan(plan: dict[str, list]) -> bool:
    print("suggested plan of organizing:")
    for category, file_list in plan.items():
        print(f"---- category: {category} ----")
        for file in file_list:
            print(f"-> {file}")
    return input("confirm execution of the organizing plan? (y/n): ").lower() == "y"
