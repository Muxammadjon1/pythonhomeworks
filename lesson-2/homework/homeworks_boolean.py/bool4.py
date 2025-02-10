a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

if a == b and b == c:
    print("All of them are the same")
elif a != b and b != c and a != c:
    print("All of them are different")
else:
    print("Some of them are the same")