#join을 사용한 풀이

import sys
input = sys.stdin.readline

M, N, K = map(int,input().split())
secret = "".join(list(input().strip()))
user_did = "".join(list(input().strip()))
if secret in user_did:
    print("secret")
else:
    print("normal")
