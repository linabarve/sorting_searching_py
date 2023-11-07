		# linear search.........

n = int(input("Enter the number of element:"))
a = []
for i in range(n):
	k = int(input())
	a = a + [k]
	
p = int(input("enter the find number:"))
f = 0

for i in range(n):
	if a[i] == p:
		f = f + 1
if(f):
	print("Element present in this list:",p)
else:
	print("Element not preset in this list:",p)
	
	
		
