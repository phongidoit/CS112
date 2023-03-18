#phân tích độ phức tạp của các hàm sau, deadline 23:59:59 26/03/2023 UTC+7

def bt1(n):
    if n==1:
        return n
    else:
        return (n//3)+(n//2)

def bt2(n):
    if n <= 1:
        return 1
    a = 0
    for i in range(n):
          a+=1
    return a + (n-2)

def bt3(l, r):
    if l>=r:
        # O(1) operation
    else:
        bt3( l, (r+l)//2 )
        bt3( (r+l)//2+1, r )


