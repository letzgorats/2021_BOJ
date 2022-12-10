import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b 
    

N = int(input())    # 도시의 수 N
M = int(input())    # 여행계혹에 속한 도시들의 수 M

graph = [[] for _ in range(N+1)]    # 도시 번호는 1부터니까, 0번째에는 빈 리스트로 초기화
parent = [k for k in range(N+1)]    # 0부터 N까지의 도시의 부모를 자기 자신으로 초기화
# print(parent)
for i in range(1,N+1):
    row = list(map(int,input().strip().split()))
    graph[i].append(row)
 
    for idx,j in enumerate(row):
        if j == 1:  # 연결되어 있다면
            # i와 idx+1 도시 집합 합치기
            union_parent(parent,i,idx+1)  # idx+1(도시번호는 1부터이므로 각 도시번호에 +1 을 해줘야 한다.i는 이미 해당작업 처리)
                                        
plan = list(map(int,input().strip().split()))

cycle = True    # 같은 집합(같은 사이클)인지 판별하는 변수
for idx, city in enumerate(plan[:-1]):
    # 여행계획의 나라의 부모가 같지않으면,(다른집합이라면)
    if (find_parent(parent,city) != find_parent(parent,plan[idx+1])):
        cycle = False   # 다른집합이다.

if cycle == True: # 같은집합이면 여행가능
    print("YES")
else:
    print("NO")
