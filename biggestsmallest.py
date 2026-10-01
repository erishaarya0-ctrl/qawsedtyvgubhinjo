arr=[]
p=int(input('how many numbers do you want:'))
for i in range(p):
    x=int(input('enter a number:'))
    print(x)
    arr.append(x)
print(arr)
arr.sort()
n=len(arr)
print('the biggest number is:',arr[n-1],'the smallest number is:',arr[0])
