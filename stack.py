a=input("enter brackets : ")
b=[]
for i in range(len(a)):
    if a[i] in "{[(":
        b.append(a[i])
    elif a[i]=="}" and b[-1]=="{":
        b.pop()
    elif a[i]==")" and b[-1]=="(":
        b.pop()
    elif a[i]=="]" and b[-1]=="[":
        b.pop()
    else:
        break
if len(b)==0:
    print(-1)
else:
    print([i+1])
    
#_______________________________________________________#
a='bbbcbcbcncncnbchfhcncjvhvha'
b=' '
for i in a:
    if i not in b:
        b=b+i
for i in b:
    print(i,"-",a.cout(i))
