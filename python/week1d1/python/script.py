Input = "stringwithoutnum"
for ch in Input:
    flag = False
    if ch.isnumeric():
        flag = True
        break
print(flag)