"""		 #Selection sort.......

n = [7,6,3,4,1]
n.sort()
print(n)


		# selection sort using while loop...........

n = int(input("Enter the value of n: "))
a = []

# Input the elements into the list
i = 0
while i < n:
    k = int(input())
    a = a + [k]
    i = i + 1

i = 0
while i < n:
    m = i
    j = i + 1
    while j < n:
        if a[j] < a[m]:
            m = j
        j = j + 1

    # Swap the minimum element with the current element
    temp = a[i]
    a[i] = a[m]
    a[m] = temp

    i = i + 1

print("Sorted list:", a)


