b=0
for i in range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end="")
    print("\r")
print("------------")
for i in range(5,0,-1):
    for j in range(0,i):
        print(5,end="")
    print("\r")