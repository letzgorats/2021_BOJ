import sys
input = sys.stdin.readline

month, day = map(int,input().split()) # 월과 일 입력받기
total_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]   # 1월~12월 마다의 총 일수
day_of_week = ['MON','TUE','WED','THU','FRI','SAT','SUN'] # 요일별 리스트
start = 'MON' # 시작은 MON(월요일)이므로 그냥 표시용 변수(활용은 X) - 1월 1일의 요일을 첫 인덱스로 설정하면 용이
days = 0  # 1월 1일부터 입력된 x월 y일까지 총 일수 구하기 위한 days 변수
for i in range(1,month): # 직전달까지의 일수 더하기
    days += total_day[i]

days += day # 해당 달의 일 수까지 더하기

print(day_of_week[days % 7 -1]) # 요일별 리스트의 길이만큼의 나머지에서 1을 빼야한다.(인덱스 때문에)
