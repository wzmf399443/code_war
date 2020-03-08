def digital_root(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
        print(ans,n)
    return ans if ans < 10 else digital_root(ans)

print(digital_root(456))

'''
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
'''