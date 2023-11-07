
	# Insertion sort..................

n = int(input("Enter the number of elements: "))
a = []

for _ in range(n):
    element = int(input("Enter an element: "))
    a.append(element)

for i in range(1, n):
    temp = a[i]
    j = i
    while j > 0 and a[j - 1] > temp:
        a[j] = a[j - 1]
        j -= 1
    a[j] = temp

print("Sorted array:")
for j in range(n):
    print(a[j], end=" ")


