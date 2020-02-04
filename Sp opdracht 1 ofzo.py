a = int(input("Geef nummer"))

for i in range(a):
    print("*"*(i+1))
for i in range(a):
    print("*"*(a-i-1))

i = 1
while i != a+1:
    print("*"*i)
    i += 1
i = 1
while i != a:
    print("*"*(a-i))
    i += 1

for i in range(a):
    print(" "*(a-i-1)+"*"*(i+1))
for i in range(a):
    print(" "*(i+1)+"*"*(a-i-1))

i = 1
while i != a+1:
    print(" "*(a-i)+"*"*(i))
    i += 1
i = 1
while i != a:
    print(" "*(i)+"*"*(a-i))
    i += 1