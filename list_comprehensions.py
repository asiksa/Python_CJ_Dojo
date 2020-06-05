#[1, 4, 9, 16, 25, 36]
#[36,25,16,9,4,1]

a=[]
for x in range(1,7):
  a.append(x**2)
print(a)

#[1, 4, 9, 16, 25, 36]

a=[x**2 for x in range(1,7)]
print(sorted(a, reverse=True))
#[36, 25, 16, 9, 4, 1]

b=[]
for x in range(6,0,-1):
  b.append(x**2)
print(b)

#[36, 25, 16, 9, 4, 1]

b=[x**2 for x in range(6,0,-1)]
print(b)

#[36, 25, 16, 9, 4, 1]
