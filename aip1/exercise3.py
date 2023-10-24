n = int(input('Enter a positive number: '))
a = 0

while a**2 <= n/3:
    b=a
    while b**2 <= (n-a**2)/2:
        c=b
        while c**2 <= (n-a**2-b**2):
            if a**2+b**2+c**2 == n:
                print(a, b, c)
            c+=1
        b+=1
    a+=1

