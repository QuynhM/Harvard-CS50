#method 1
from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(n):
    print((n - 1 - i) * " ", end="")
    print((i + 1) * "#", end="")
    print("  ", end="")
    print((i + 1) * "#")
    
#method 2
while True:
    n = int(input("Height: "))
    if n > 0 and n < 9:
        break

for i in range(1, n+1):
  space, star = " "*(n-i), "#"*i
  print(space + star + " " + star + space)
