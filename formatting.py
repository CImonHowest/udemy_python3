for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}"
          .format(i, i ** 2, i ** 3))

print("\n-------------------------\n")

# :2, :4 geven de spacing weer om het te displayen in de terminal (field width)
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print("\n-------------------------\n")

# :2, :4 geven de spacing weer om het te displayen in de terminal (field width), < zorgt voor de left align
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}"
          .format(i, i ** 2, i ** 3))

print("\n-------------------------\n")

# :2, :4 geven de spacing weer om het te displayen in de terminal (field width), ^ zorgt voor de center align
for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))

print("\n-------------------------\n")

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print("\n-------------------------\n")

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:}"
          .format(i, i ** 2, i ** 3))

    print("\n-------------------------\n")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")