number = int(input('please input your number: '))
accumulator = 0
for i in range(1, number+1):
    if number%i == 0:
        accumulator+=1
if accumulator==2:
    print(' prime')
else:
    print(' not prime')