# Write a function called isUnique that uses a nested
# for loop to compare each element with every other
# element. The function should return false if there
# are any two identical values at different indexes of
# the array.
def is_unique(a):
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if (a[i] == a[j]):
                return False
    return True

if is_unique([2,2,3]):
  print("yup.")

if is_unique([1,2,3]):
  print("yup.")
