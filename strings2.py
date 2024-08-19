
#         01234567890123
#         43210987654321
parrot = "Norwegian Blue"

print(parrot)

print("----------------------------")

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("----------------------------")

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("----------------------------")

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print("----------------------------")

print(parrot[0:6]) # Norweg (up to but not including index 6)
print(parrot[-14:-8]) # Norweg
print(parrot[3:5]) # (index 3 up to but not including index 5)
print(parrot[0:9]) # (index 0 up to but not including index 9)
print(parrot[:9]) # (starting index up to but not including index 9)

print("----------------------------")

print(parrot[10:14]) # Blue (index 10 up to but not including index 14)
print(parrot[10:]) # Blue (index 10 up to but not including the end)

print("----------------------------")

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl

print("-------------Start stop and step---------------")

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])