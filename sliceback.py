#          01234567890123456789012345
#          65432109876543210987654321
letters = "abcdefghijklmnopqrstuvwxyz"

print("---------------")

backwards = letters[25:0:-1]
print(letters)
print(backwards)

print("---------------")

backwards = letters[25:-1:-1]
print(letters)
print(backwards)

print("---------------")

backwards = letters[25::-1]
print(letters)
print(backwards)

print("---------------")

backwards = letters[::-1]
print(letters)
print(backwards)

print("-------Challenge--------")
# qpo
backwards = letters[16:13:-1]
print(backwards)

# edcba

backwards = letters[4::-1]
print(backwards)

# De laatste 8 chars omgekeerd

backwards = letters[:-9:-1]
print(backwards)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
