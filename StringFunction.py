def functions():
    str=input("enter the string")
    return str
def f1():
    p=functions()
    print("function name:capitalise")
    x=p.capitalise()
    return x

def f2():
    p=functions()
    print("function name:istitle")
    x=p.istitle()
    return x
def f3():
    p=functions()
    print("function name:split")
    x=p.split(' ')
    return x
def f4():
    p=functions()
    print("function name:upper")
    x=p.upper()
    return x
def f5():
    p=functions()
    print("function name:title")
    x=p.title()
    return x
def f6():
    p=functions()
    print("function name:strip")
    a=input("which letter to remove")
    x=p.strip(a)
    return x
def f7():
    p=functions()
    print("function name:islower")
    x=p.islower()
    return x
def f8():
    p=functions()
    print("function name:isalpha")
    x=p.isalpha()
    return x
def f9():
    p=functions()
    print("function name:replace")
    c=input("which word want to change from the string")
    d=input("which word replace")
    x=p.replace(c,d)
    return x
def f10():
    p=functions()
    print("function name:swapcase")
    x=p.swapcase()
    return x
print("****string functions****")
print("\n1.to capitalise the word\n2.istitle\n3.split\n4.upper\n5.title\n6.strip\n7.islower\n8.isalpha=\n9.replace\n10.swapcase")
s=int(input("enter the option"))
funcs=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
output=funcs[s-1]()
print(output)
r=input("do you want to repeat yes/no:")
while r=='yes':
    s=int(input("enter the option"))
    funcs=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    output=funcs[s-1]()
    print(output)
