#4, 3 5, 2 6, 1 7, 012345678 
n = int(input("請輸入三角形的高度:"))
if(n < 2) : 
    print("輸入錯誤")
else :
    print(" "*(n-1) + "*")
    x = 0
    for i in range(1, n-1):
        for j in range(n + i):
            if(abs(j - n + 1) == i):
                print("*", end = "")
            else: print(" ", end = "")
        print()
    print("*" * (2*n-1), end = "")