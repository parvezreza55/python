# lists:

subject=['apple','banana','mango','lime','pineapple']
print(subject)
print(subject[:-2])
print(subject[1:4])

# to find the element in a list
print("banana" in subject)
print("apple" not in subject)

# to add more elements in the same list
print(subject + [10,"cats","hair"])

# to copy full elements and how times whole elements to copy

print(subject * 3)

# length of list
print(len(subject))
subject.append("pineapple")
print(subject)