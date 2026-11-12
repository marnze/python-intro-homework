# Error:
# Traceback (most recent call last):
#   File "C:\Users\nunez\Desktop\python_class\python-intro-homework\week-6\assignment-6\warmup3.py", line 5, in <module>
#     print(message)
#           ^^^^^^^
# NameError: name 'message' is not defined

def greeting():
    message = "Hello"
    return message

message = greeting()
print(message)