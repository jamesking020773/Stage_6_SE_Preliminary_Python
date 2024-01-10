list1=[1,7,3,'a','x','p',4.6,0.2,3.7]
print(list1)

list1.append(2.3)
print("list1.append(2.3)")
print(f"Current list: {list1}")

list1.insert(2,0.9)
print("list1.insert(2,0.9)")
print(f"Current list: {list1}")

list1.pop()
print("list1.pop()")
print(f"Current list: {list1}")

list1.remove('x')
print("list1.remove('x')")
print(f"Current list: {list1}")

list1.pop(4)
print("list1.pop(4)")
print(f"Current list: {list1}")

print("len(list1)")
print(f"Length of current list = {len(list1)}")

list2=[1,5,3,9,0]

list2.sort()
print("list2.sort()")
print(f"Current list: {list2}")


print("list2.index(3)")
print(f"Index: {list2.index(3)}")

list2.append(3)
print("list2.append(3)")
print(f"Current list: {list2}")

list2.count(3)
print("list2.count(3)")
print(f"Current list: {list2}")

list2.sort(reverse=True)
print("list2.sort(reverse=True)")
print(f"Current list: {list2}")


# Common built-in functions in Python for lists.
#1. append(): This function is used to add an element to the list at the end.
#2. insert(): This function takes the element and the index as arguments and inserts the value in the specified location.
#3. pop(): This function deletes the last element if no index passes or deletes the element at that index and returns it.
#4. remove(): This function removes the specified value from the list.
#5. len(): This function returns the length or number of elements in the list
#6. sort(): This arranges the elements of the list in ascending or descending order
#7. index(): This is used to find the index of the element passed
#8. count(): This finds the number of times the value occurs in a list
