# Output
# {'Java', 'C++', 'C', 'Scala', 'Python'}
# {'C++'}
# {'C', 'Java'}
lst1 = ["C", "C++", "Java"]
lst2 = ["C++", "Scala", "Python"]
print(set(lst1).union(lst2))
print(set(lst1).intersection(lst2))
print(set(lst1).difference(lst2))