def solution(phone_book):
    phone_book = sorted(phone_book)  # phone_book을 정렬한다.
  
    answer = True # 초기 answer 값을 True로 설정하고
    for idx in range(len(phone_book)-1):  # phone_book 리스트 길이 바로 전까지 만큼 for문을 돈다(idx+1에서 인덱스 오류 방지를 위해)
        # 지금 바라보고 있는 phone_book[idx]와 바로 다음 번호를 비교하되, 접두어이므로, [:len(phone_book[idx])]으로 슬라이싱 해준다.
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:  
            answer = False  # 해당 번호가 다음 번호의 접두어가 되는 순간 answer은 False 가 된다
            break # for문 탈출
        
    return answer # answer 리턴
  
  # 이 외에도 "스트링.startswith" 함수나 for p1, p2 in zip(phoneBook, phoneBook[1:]) 등으로 풀 수도 있다.

