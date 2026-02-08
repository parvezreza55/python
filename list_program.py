# lists:

subject=['apple','banana','mango','lime']
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

# to add one element one the last
subject.append("pineapple")
print(subject)

# To add manually on the specific index use insert(index_no,"elements")
subject.insert(2,"orange")
print(subject)

# To remove any elements use remove("name")
subject.remove("pineapple")
print(subject)

# TO sort any list use .sort()
subject.sort()
print(subject)

#copy index and count
pos=subject.index("apple")
print(pos)

subject2=subject.copy()
print(subject2)

counts =subject.count("apple")
print(counts)

