#print sum of digits of given number
n=int(input())
sum=0
while(n):
	r=n%10
	sum += r
	n=n//10
print(sum)