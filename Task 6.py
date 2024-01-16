#Q1. a Python list[10, 501, 22, 37, 100, 999, 87, 351] to create two list , one which have all Even numbers and another list which have all the Odd numbers in it.#

myList = [10, 501, 22, 37, 100, 999, 87, 351]

# Separate even and odd numbers into two lists
even_numbers= []
odd_numbers= []

for i in myList:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

# Print the results
print("Original List:", myList)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

#Q2. a Python List[10, 501, 22, 37, 100, 999, 87, 351] to Count all the Prime numbers and create a new Python list which will contain all the Prime Numbers in it.#

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in original_list if isPrime(num)]
prime_count = len(prime_numbers)

# Print the results
print("Original List:", original_list)
print("Prime Numbers List:", prime_numbers)
print("Count of Prime Numbers:", prime_count)

#Q3. a Python List[10,  501 , 22,  37,  100,  999,  87,  351]  Find out how many numbers are there in the given Python list which are Happy Numbers?#

def happyNumber(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

my_list = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in my_list if happyNumber(num)]
happy_count = len(happy_numbers)

# Print the results
print("Original List:", my_list)
print("Happy Numbers List:", happy_numbers)
print("Number of Happy Numbers:", happy_count)

#Q4. a python program to find the sum of the first and last digit of an integer?#

def sum_of_first_and_last_digit(integer):
    # Convert the number to a string to access digits
    num_str = str(integer)

    # Extract the first and last digits
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])

    # Calculate the sum of the first and last digits
    result = first_digit + last_digit
    return result

integer = 54871

result_sum = sum_of_first_and_last_digit(integer)
print(f"Sum of the first and last digit: {result_sum}")

#Q5.a list of N integers which represents the number of  Mangoes in a Bag. Each bag has a variable number of Mangoes. There are M students in Guvi class, your task is to distribute the Mangoes in such a way that each student gets one bag. The difference between number of Mangoes in a bag with maximum Mangoes and bag with minimum Mangoes given to the student is minimum?#

def distributeMangoes(bags, students):

    if len(bags) < students:
        return "Not enough bags for all students"
    
    bags.sort()  # Sort the bags in ascending order

    min_difference = float('inf')
    min_index= 0

    for i in range(len(bags) - students + 1):
        difference = bags[i + students - 1] - bags[i]
        if difference < min_difference:
            min_difference = difference
            min_index = i

    result = bags[min_index:min_index + students]
    max_mangoes = max(result)
    min_mangoes = min(result)

    return result, f"The difference between the bag with maximum mangoes ({max_mangoes}) and the bag with minimum mangoes ({min_mangoes}) given to the students is minimum."

bags = [9, 6, 3, 9, 15, 11]
students = 5

result, output_message = distributeMangoes(bags, students)
print("Bags to distribute:", result)
print(output_message)

#Q6. given three lists. Your task is to find the duplicates in the three lists. Write a python program for the same. You can use your own python lists. #

def Duplicates(list1, list2, list3):
    
    all_lists = list1 + list2 + list3

    #a dictionary to store the count of each element
    element_count = {}

    #List to store duplicates
    duplicates = []

    for element in all_lists:
        if element in element_count:
            if element not in duplicates:
                duplicates.append(element)
        else:
            element_count[element]= 1

    return duplicates

list1 = [6, 9, 15, 18, 20]
list2 = [5, 9, 15, 17, 19]
list3 = [6, 8, 11, 18, 20]

result = Duplicates(list1, list2, list3)
print("Duplicates:", result)

#Q7. a python program to find the first non- repeating elements in a given list of integers.#

def first_non_repeating_element(nums):
    element_count = {}

    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    for num in nums:
        if element_count[num] == 1:
            return num
    
    return None  # If no non-repeating element is found

numbers = [2, 3, 4, 5, 2, 3, 4, 6, 8, 7]
result = first_non_repeating_element(numbers)

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found in the list.")

#Q8. a python program to find the minimum element in a rated and sorted list.#
    
def minimumElement(sorted_list):
    if not sorted_list:
        return None  
    else:
        return sorted_list[0]

sorted_ratings = [3, 5, 8, 14, 17, 18]
minimum_element = minimumElement(sorted_ratings)

if minimum_element is not None:
    print("Minimum element in the sorted list:", minimum_element)
else:
    print("The list is empty.")

#Q9.a Python list [ 10, 20, 30, 9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value?#
    
def triplet_with_sum(lst, value):
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst) - 1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == value:
                    return lst[i], lst[j], lst[k]
    return None

given_list = [10, 20, 30, 9]
value = 59

result= triplet_with_sum(given_list, value)

if result is not None:
    print(f"Triplet with sum {value} found:", result)
else:
    print(f"No triplet found with sum {value}.")

#Q10. a list [ 4, 2, -3, 1, 6] Write a python program  to find if there is a sub- list with sum equal to zero.#
    
def sublist_with_sum_zero(lst):
    prefix_sum = set()
    current_sum = 0

    for num in lst:
        current_sum += num

        if current_sum == 0 or current_sum in prefix_sum:
            return True
        
        # Add the current sum to the set
        prefix_sum.add(current_sum)

    # If no sublist with sum zero is found
    return False

given_list = [4, 2, -3, 1, 6]
result = sublist_with_sum_zero(given_list)

if result:
    print("There is a sub-list with sum equal to zero", result)
else:
    print("No sub-list with sum zero found.")






