a = int(input("Geef nummer"))

for i in range(a):
    print("*"*(i+1))
for i in range(a):
    print("*"*(a-i-1))

i = 1
while i != a:
    print("*"*i)
    i += 1
i = 1
while i != a:
    print("*"*(a-i))
    i += 1