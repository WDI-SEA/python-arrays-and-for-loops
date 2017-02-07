# Write a function called isUnique that uses a nested
# for loop to compare each element with every other
# element. The function should return false if there
# are any two identical values at different indexes of
# the array.
def is_unique(a):
    for x in range(0,len(a)):
        for y in range(0,len(a)):
            if (x != y):
                if (a[x] == a[y]):
                    return False
    return True

if is_unique([2,2,3]):
    print("yup.")
else:
    print('nope')

if is_unique([1,2,3]):
    print("yup.")
else:
    print('nope')
