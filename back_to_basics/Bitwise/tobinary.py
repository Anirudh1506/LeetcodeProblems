def to_binary(n):

    res=''
    while n!=0:
        res+=str((n%2))
        n=n//2
    print(res[::-1])


if __name__=='__main__':
    n=int(input())
    to_binary(n)