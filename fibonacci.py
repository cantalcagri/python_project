list_fibo = [1, 1]
i = 2
while True:
    list_fibo.append(list_fibo[i-1]+ list_fibo[i -2])
    print(list_fibo)
    i += 1
    if list_fibo[-1] == 55:
        break