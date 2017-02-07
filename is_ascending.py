def is_ascending(a):
    for num in range(1,len(a)):
        if (a[num-1] > a[num]):
            return False
    return True

a1 = [1, 2, 3, 4, 8, 10];
a2 = [1, 2, 3, 4, 8, 6, 10];
if is_ascending(a1):
    print("a1 is ascending!!")
else:
    print("a1 is NOT ascending!!")

if is_ascending(a2):
    print("a2 is ascending!!")
else:
    print("a2 is NOT ascending!!")
