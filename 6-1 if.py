# if문 -> input으로 상태 작성, 작성시 한칸은 띄어넣기(문장형, 숫자입력시 int로 정수화 시켜야함), if -> elif -> else 순으로 작성 
#weather = input("오늘의 날씨는 어떤가요? ")
#if weather == "비":
#    print("우산을 챙기세요!")
#elif weather == "미세먼지":
#    print("마스크를 챙기세요!")
#else :
#     print("준비물이 없어요!")

temp = int(input("오늘의 기온은 몇도인가요? "))
if temp >= 30:
    print("더우니까 나가지 마세요!")
elif temp <30 and temp >= 20:
    print("날씨가 아주 좋아요!")
elif temp < 20 and temp >= 10:
    print("날씨가 쌀쌀해요!")
else:
    print("추우니까 나가지 마세요!") 


