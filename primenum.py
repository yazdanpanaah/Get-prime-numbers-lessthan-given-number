def check_prime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
def return_prime(n):
    for i in range(2, n + 1):
        if check_prime(i):
            yield i

get_num = int(input('enter num:'))
for i in return_prime(get_num):
    if i<get_num:
        print(i)
