for i in range(1,10):
    for j in range(1,4):
      for k in range (1,4):
           if i <= 3 and j == 1 and k == i: 
                print(f"{i}, {j}, {k}")
                break 
           elif 4 <= i <= 6 and j == 2 and k == (i - 3): 
                print(f"{i}, {j}, {k}")
                break 
           elif 7 <= i <= 9 and j == 3: 
                print(f"{i}, {j}, {k}")
                break