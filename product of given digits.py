#product of given digits
n=int(input())
product=1
while(n):
	r=n%10
	product*=r
	n=n//10
print(product)