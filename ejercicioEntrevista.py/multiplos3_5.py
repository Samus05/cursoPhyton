i=0
while i <= 15:
    if i%3 == 0 and i%5 ==0:
        print('FizzBuzz\n')
        i+=1
        continue
    elif i%3==0:
        print('Fizz')
        i+=1
        continue
    elif i%5==0:
        print('Buzz')
        i+=1
        continue
    else:
        print(i)
        i+=1
        continue


