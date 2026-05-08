n = int(input("Enter the number of elements (n): "))
raw_input = input(f"Enter {n} integers separated by spaces: ")
numbers = list(map(int, raw_input.split()))
transformed_list = [x**2 if x % 2 == 0 else x**3 for x in numbers]
result = tuple(transformed_list)
print("\nResulting Tuple:")
print(result)
