"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    else: 
        retun count_even(numbers[1:])


def find_strings_with(strings, target):
    if len(strings) == 0: 
        return []

    rest = find_strings_with(strings[1:], target) 

    if target in strings[0]:
        return [strings[0]] + rest
    else: 
        return rest 

# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    if os.path.isfile(directory_path):
        return 1

    count = 0
    items = os.listdir(directory_path) 

for item in items: 
    item_path = os.path.join(directory_path, item) 
    count += count_files 

return count 
    
# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
  if os.path.isfile(directory_path):
      if directory_path.endswith(extension):
          return [directory_path]
      else: 
            return []

    infected = []
    items = os.listdir(directory_path) 

    for item in items:
        item_path = os.path.join(directory_path, item)
        infected.extend(find_infected_files(item_path, extension))

    return infected

# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - FINAL CODE\n")
    print("Complete the functions above, then run this file to test your work.\n")
    
    print("Test Case Results:")
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    print("\nInfected File Tests:")
    print("Test Case 1:", len(find_infected_files("test_cases/case1_flat")))  # 0
    print("Test Case 2:", len(find_infected_files("test_cases/case2_nested")))  # 0
    print("Test Case 3:", len(find_infected_files("test_cases/case3_infected")))  # 3

    print("\n--- Breach Data Analysis ---")
    total_files = count_files("breach_data") 
    infected_files = find_infected_files("breach_data") 

    print("Total files:", total_files)
    print("Total infected files:", len(infected_files))

    print("\n--- Department ANalysis ---")
    finance = len(find_infected_files("breach_data/Finance"))
    hr = len(find_infected_files("breach_data/JR"))
    sales = len(find_infected_files("breach_data/Sales"))

    print("Finance infected:", finance)
    print("HR infected:", hr)
    print("Sales infected:", sales)

    print("\n Done! Copy these numbers into your document.")
    
    
 
