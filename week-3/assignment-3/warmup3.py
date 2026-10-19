print(not True and False) # False - (not True) -> False, False and False -> False
print(True or False and False) # True - (False and False) -> False, True or False -> True 
print(not (5 > 3)) # False - (5 > 3) -> True, not True -> False
print(10 == 10 and 4 != 4) # False - (10 == 10) -> True, (4 != 4) -> False, True and False -> False
print(not False or not True) # True - (not False) -> True, (not True) -> False, True or False -> True