		# Binary search.........

n = int(input("Enter the number of elements: "))
a = []


for i in range(n):
    p = int(input("Enter element {}:".format(i + 1)))
    a.append(p)

k = int(input("Enter the number to find: "))
s = 0
e = n - 1
f = 0

while s <= e:
    m = (s + e) // 2

    if a[m] == k:
        f = 1
        print("Element {} found at index {}.".format(k, m))
        break
    elif a[m] < k:
        s = m + 1
    else:
        e = m - 1

if f == 0:
    print("Element {} not found in the list.".format(k))

