# continue는 주어진 사람을 제외하고 끝날때까지 반복한다.
# break는 주어진 작업을 도중에 멈추는 기능을 한다.
absent = [2,4,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지, {0} 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어보렴".format(student))










