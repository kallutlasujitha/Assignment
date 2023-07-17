#Assignment-1 output:boy good is ram
a='ram is good boy'
b=a.split()
c=b[::-1]
d=(" ".join(c))
print(d)

#Assignment-2 output:ABCDEFGHI
s="ABCDAABBCCDDEEFFGGHI"
p=[]
for j in s:
    if j not in p:
        p.append(j)
x="".join(p)
print(x)


