n = int(input("請輸入 n:\n"))
number = input("請輸入數列:\n").split(" ")
print(f"排序前的數列: {' '.join(number)}")
number = [int(x) for x in number]
number.sort()
number = [str(x) for x in number]
print(f"排序後的數列: {' '.join(number)} ")
