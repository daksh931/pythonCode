a = int(input ('Enter First number - '))
b = int(input ('Enter Second number - '))
c = int(input ('Enter Third number - '))

if a<b and a<c:
    print(a)
    if b<c:
        print(b)
        print(c)
    elif c<b:
        print(c)
        print(d)
        
elif b<a and b<c:
    print(b)
    if a<c:
        print(a)
        print(c)
    elif c<a:
        print(c)
        print(a)

elif c<a and c<b:
    print(c)
    if a<b:
        print(a)
        print(b)
    elif b<a:
        print(b)
        print(a)

