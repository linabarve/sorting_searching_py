		# BUBBLE SHORT USING SORT FUNCTION.....
 
l = [5,6,10,5,8]
l.sort()
print(l) 

		#  bubble shor user input using while loop........

n =  int(input("enter the number:"))
a = []
i = 0
while i < n:
	k = int(input("enter the number:"))
	a =  a + [k]
	i = i + 1
i = 0
while i < n:
	j = 0
	while j < n-i-1:
		if a[j] > a[j+1]:
			temp = a[j]
			a[j] = a[j + 1]
			a[j + 1] = temp
		j = j + 1
	i = i + 1
print(a)
		 


		# bubble sort user input for loop use.......

n = int(input("Enter the value:"))
a =  []
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







