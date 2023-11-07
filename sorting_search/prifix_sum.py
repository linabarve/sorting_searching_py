		#prinfix sum......
n = int(input("Enter the number of elements: "))
a = []


for i in range(n):
    k = int(input("Enter a number: "))
    a.append(k)

k, p = map(int, input("Enter the values of k and p: ").split())
s = 0

if 0 <= k and 0 <= p:
    while k <= p:
        s += a[k]
        k += 1
    print("Sum of elements from index", k, "to", p, "is:", s)
else:
    print("Invalid indices. Please enter valid indices.")


