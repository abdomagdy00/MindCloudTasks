
try:
    print("Enter Value Of K: ")
    k_str=input()
    print("Enter Value Of m: ")
    m_str = input()
    k = int(k_str)
    m = int(m_str)
except (ValueError, IndexError):
    print("Error in input format !!")
    exit()

# List to store all input lists
lists_of_numbers = []

for _ in range(k):
    try:
        line_input = list(map(int, input().split()))
        # The first number is N (count), the rest are the elements
        lists_of_numbers.append(line_input[1:])
    except (ValueError, IndexError):
        print("Error in list input format.")
        exit()

# We use a global variable because the recursive function doesn't return a value directly
max_s_value = 0

# ------------------------------------------------------------------
# Recursive function to generate combinations and find the max value
# ------------------------------------------------------------------
def find_max_s(list_index, current_sum):
    global max_s_value

    # Base Case: When we have processed all lists
    if list_index == k:
        current_s = current_sum % m
        if current_s > max_s_value:
            max_s_value = current_s
        return

    # Recursive Step: Loop through the elements of the current list
    for element in lists_of_numbers[list_index]:
        # Call the function for the next list, adding the square of the current element
        find_max_s(list_index + 1, current_sum + element**2)


# --- Start the calculation process ---

# Initial call to the recursive function
# Start with the first list (index 0) and an initial sum of 0
find_max_s(0, 0)

print(max_s_value)