
# 0,1,1,2,3,5,8,13
# 0,1,2,3,4,5,6,7
def fibo(n):
    if n==0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)


# 0,1,3,6,10,15,21, 28
# 0,1,2,3,4 ,5,6, 7
def add_prior(n):
    if n == 0:
        return 0
    return add_prior(n-1) + n





if __name__ == "__main__" :
    # res = fibo(7)
    res = add_prior(7)
    print(res)
