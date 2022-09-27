import sys
input = sys.stdin.readline

height = []
for _ in range(9):
    height.append(int(input()))

diff = sum(height)-100  # 9명의 난쟁이 키의 합과 100의 차이를 구한다
find_two_false = False  # find_two_false라는 초기변수를 False로 설정한다.

for i in height:
    for j in height[1:]:
        if i + j == diff: # height를 돌면서 두 난쟁이의 합이 diff와 같으면
            height.remove(i)  # 그 난쟁이들은 가짜 난쟁이이므로 제거
            height.remove(j)  
            find_two_false = True # 두 가짜 난쟁이를 찾았으니 find_two_false라는 초기변수를 True로 설정한다.
            break
    if find_two_false == True:  # 두 가짜 난쟁이를 찾았으면
        height.sort()           # 정렬하고
        print(*height,sep="\n") # 한 줄에 하나씩 출력, *를 사용할 때는 sep 사용
        break
