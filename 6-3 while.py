# while -> 한 행동을 끝날때까지 무한히 반복하는 것

#starbucks = ["유재석", "정형돈", "노홍철"]
#for customer in starbucks:
#    print("{0}, 주문하신 커피가 나왔습니다.".format(customer)) 

#customer = "토르"
#index = 5
#while index >= 1:
#    print("{0}, 주문하신 커피가 나왔습니다. {1}번 남았습니다.".format(customer,index))
#    index -= 1  #숫자에서 1씩 내릴때 -=로 표현
#   if index == 0:
#        print("커피가 폐기처분 되었습니다.")
# 무한루프, true 사용 -> 강제 종료(Ctrl + C)
#customer = "아이언맨"
#index = 1
#while True:
#    print("{0}, 주문하신 커피가 나왔습니다. {1}번 남았습니다.".format(customer,index))
#    index += 1


# 카운터에 손님이 왔을때 구별하는 방법

customer = "토르"
person = "Unknown"
while person != customer:
    person = input("이름이 어떻게 되세요? ")
    print("{0}, 주문하신 커피가 나왔습니다.".format(customer))
    








