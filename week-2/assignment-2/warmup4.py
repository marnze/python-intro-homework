# 1. Error output:
# Traceback (most recent call last):
#   File "C:\Users\nunez\Desktop\python_class\python-intro-homework\week-2\assignment-2\warmup4.py", line 1, in <module>
#     print(f"Your age is {age}")
#                          ^^^
# NameError: name 'age' is not defined
# 2. NameError, age variable hasn't been defined yet
# 3. Defined the age variable 
birth_year = int(input("What year were you born? "))
age = __import__("datetime").datetime.now().year - birth_year
print(f"Your age is {age}")
