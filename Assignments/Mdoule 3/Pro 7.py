#Write a Python program to remove duplicates from a list. 


def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:   #Here I have used membership operator to find duplicate in the list.
            output_list.append(item)
    return output_list

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
result_list = remove_duplicates(input_list)
print("Original list:", input_list)
print("List with duplicates removed:", result_list)
