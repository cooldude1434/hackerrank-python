for i in range(int(input())):
    n,A=input(),set(input().split())
    n,B=input(),set(input().split())
    print(A.issubset(B))
