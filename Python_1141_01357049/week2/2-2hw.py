arr = []
num = 0
while True:
    try:
        n = int(input("請輸入一個數:"))
        arr.append(n)
        arr.sort()
        if(len(arr) %2 == 1):
            print(arr[len(arr)//2])
        else :
            print((arr[len(arr)//2] + arr[len(arr)//2 - 1]) //2)
    except EOFError:
        break
