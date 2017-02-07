def is_ascending(a):
    if sorted(a) == a:
        return True
    else:
        return False

a1 = [1, 2, 3, 4, 8, 10];
a2 = [1, 2, 3, 4, 8, 6, 10];
if is_ascending(a1):
  print("a1 is ascending!!")

if is_ascending(a2):
  print("a2 is ascending!!")
