def print_exactly_twice(L):    
    counts = {}
    for num in L:
        counts[num] = counts.get(num, 0) + 1  
    
    seen = set()
    result = []
      
    for num in L:
        if counts[num] == 2 and num not in seen:
            result.append(num)
            seen.add(num)
    
    if result:
        print(*(result))


user_input = input("Enter your numbers separated by spaces: ")


L = [int(x) for x in user_input.split()]


print_exactly_twice(L)
