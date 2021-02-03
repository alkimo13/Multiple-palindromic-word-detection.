def ispaly(st1):
    if st1[::-1] == st1:
        return True
    else:
        return False
a =  "Madam Tssaud has just came from kayak. Her daughter Anna was waiting her mom while the phone rang"
aa = []
b = 0
x =0
y = 1
a = a.lower()
while y<len(a)+1:
    aa.append(a[b:y])
    y = y+1
    if y == len(a)+1:
        b=b+1
        y =b+1
for i in list(set(aa)):
    if ispaly(i) and len(i)>1:
        print(i.strip())
