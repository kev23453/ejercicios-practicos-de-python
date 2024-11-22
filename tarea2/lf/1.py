for i in range(0,10):
    for j in range(1,6):
        if i%2==0:
            j=i//2+1
        else:
            j= (i+1)//2
    print(f"{i},{j}")