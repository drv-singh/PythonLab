def Prime(n):              #Function to check if no is prime or not
    if n <= 1 : 
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False
    return True
t=int(input())             #No.of test cases
for x in range(t):
    while(1):
        m,n = map(int,input().split())  #to check if m and n are correctly entered
        if m<1 or n>1000000000 or m>n or n-m>100000:
            print('Incorrect value for m and/or n, Re-enter!')
            continue
        else:
            break
    a=list(range(m,n+1))      #create a list of prime no in range of m & n
    for i in range(m,n+1):
        if Prime(i):
            continue
        else:
            a.remove(i)
    print('Output: ')     
    print(m,n)
    print(a)       #print the list


