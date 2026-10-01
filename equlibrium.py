arr=[]
p=int(input('how many numbers do you want:'))
for i in range(p):
    x=int(input('enter a number:'))
    print(x)
    arr.append(x)
print(arr)
k=(p//2)+1
if p%2==0:
    pass
else:
    arr.pop(k-1)
p=len(arr) 
v=int(p/2)
m=sum(arr[0:v])
n=sum(arr[v:p])
if n==m:
    print('the Array is in equilibrium')
else:
    print('The array is not in equilibrium')
