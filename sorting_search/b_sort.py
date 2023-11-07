"""l = [9,2,8,3,5,1]
l.sort()
print(l)


n = int(input())
a = []
for i in range(n):
	k = int(input())
	a = a + [k]
for i in range (n):
	for j in range(0,n-i-1):
		if a[j] > a[j + 1]:
			temp = a[j]
			a[j] = a[j +1]
			a[j + 1] = temp
print(a)

"""
	# without using third veriable......
	
n = int(input())
a = []
for i in range(n):
	k = int(input())
	a = a + [k]
for i in range (n):
	for j in range(0,n-i-1):
		if a[j] > a[j+1]:
			a[j],a[j+1] = a[j+1],a[j]
print(a)


