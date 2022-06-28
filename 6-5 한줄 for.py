# 출석부 번호에 100을 더하기로 함 ex) 1,2,3 ->101, 102, 103
student = [1,2,3,4,5]
student = [i+100 for i in student]
print(student)

# 학생이름을 길이로 변환 -> len()
student = ["iron man", "gundam", "thor"]
student = [len(i) for i in student]
print(student)

# 힉생 단어를 대문자로 변환 ->.upper()
student = ["iron man", "gundam", "thor"]
student = [i.upper() for i in student]
print(student)


