##############################
#프로그램명 : 성적관리프로그램(객체지향 프로그램으로 수정하기)
#작성자 : 소프트웨어학부 2학년/ 박재광
#작성일 : 2025/04/09
#프로그램 설명 : 키보드로부터 학번, 이름, 영어점수, C-언어점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
##############################

#학생의 정보를 객체로 저장하기위한 class선언.
class Stduent:
    def __init__(self):#저장할 학생의 정보들 초기화.
        self.student_num = None
        self.student_name = None
        self.Eng_score = None
        self.C_score = None
        self.P_score = None
        self.sum = None
        self.avg = None
        self.grade = None
        self.rank = None
    def input_data(self):#학생 정보 입력 함수
        self.student_num = int(input("학생의 학번을 입력하시오. : "))
        self.student_name = input("학생의 이름을 입력하시오. : ")
        self.Eng_score = int(input("학생의 영어 점수를 입력하시오 : "))
        self.C_score = int(input("학생의 C-언어 점수를 입력하시오. : "))
        self.P_score = int(input("학생의 파이썬 점수를 입력하시오. : "))
    def sum_score(self):#학생의 총점 계산 함수
        self.sum = self.Eng_score + self.C_score + self.P_score
    def avg_score(self):#학생의 평균 계산 함수
        self.avg = self.sum / 3
    def grade_score(self):#학생의 학점 계산 함수
        if(self.avg >= 95):
            self.grade = "A+"
        elif(95 > self.avg >= 90):
            self.grade = "A0"
        elif(90 > self.avg >= 85):
            self.grade = "B+"
        elif(85 > self.avg >= 80):
            self.grade = "B0"
        elif(80 > self.avg >= 75):
            self.grade = "C+"
        elif(75 > self.avg >= 70):
            self.grade = "C0"
        elif(70 > self.avg >= 65):
            self.grade = "D+"
        elif(65 > self.avg >= 60):
            self.grade = "D0"
        else:
            self.grade = "F"
    def print_data(self):#학생이 정보 출력 함수.
        print("학생 학번 : ",self.student_num)
        print("학생 이름 : ",self.student_name)
        print("학생의 총점 : ",self.sum)
        print("학생의 평균 : ",self.avg)
        print("학생의 학점 : ",self.grade)
        print("학생의 등수 : ",self.rank)

#학생별 등수 계산 함수(총점을 기준으로)
def Student_rank():
    Rank = 1
    current_sum = None
    for i in range(4):#총점을 기준으로 객체를 내림차순 정렬.
        for j in range(5):
            if(not(j <= i)):
                if(students[j].sum >= students[i].sum):
                    students[j],students[i] = students[i],students[j]
    for student in students:
      if(current_sum == student.sum):
          Rank -= 1#점수가 동일하면 등수를 동일하게 만들기위해 다시 - 연산을 진행.
      current_sum = student.sum
      student.rank = Rank
      Rank += 1#등수를 +1해서 한등수 내림.

#학생 정보 삭제 함수
def Remove(a,b,c,d,e):
    del a
    del b
    del c
    del d
    del e

#총점 정렬 함수
def Sum_sort():
    list = []
    list.append(a.sum)
    list.append(b.sum)
    list.append(c.sum)
    list.append(d.sum)
    list.append(e.sum)
    list.sort(reverse=True)

    for i in list:
        print(i)

#평균이 80점 이상인 학생 수 카운트 함수
def Count_avg_over():
    avg_list =[]
    avg_list.append(a.avg)
    avg_list.append(b.avg)
    avg_list.append(c.avg)
    avg_list.append(d.avg)
    avg_list.append(e.avg)  

    count = 0
    for i in avg_list:
        if(i >=80):
            count+=1
    print("평균이 80점 이상인 학생 수 : ",count)

#탐색 함수(학번, 이름을 key로)
def Research():
    std_num = int(input("탐색하고자 하는 학생의 학번을 입력하시오. : "))
    std_name = input("탐색하고자하는 학생의 이름을 입력하시오. : ")
    for student in students:
        if student.student_num == std_num and student.student_name == std_name:
            student.print_data()
            return
    print("해당 학생을 찾을 수 없습니다.")

#학생별 객체 생성
a = Stduent()
b = Stduent()
c = Stduent()
d = Stduent()
e = Stduent()

students = [a,b,c,d,e]

#학생별 정보 삽입
a.input_data()
b.input_data()
c.input_data()
d.input_data()
e.input_data()

#학생별 총점 계산
a.sum_score()
b.sum_score()
c.sum_score()
d.sum_score()
e.sum_score()

#학생별 평균 계산
a.avg_score()
b.avg_score()
c.avg_score()
d.avg_score()
e.avg_score()

#학생별 학점 계산
a.grade_score()
b.grade_score()
c.grade_score()
d.grade_score()
e.grade_score()

#학생별 등수 계산(총점을 기준으로)
Student_rank()

#학생별 정보 출력
a.print_data()
b.print_data()
c.print_data()
d.print_data()
e.print_data()

#총점 정렬 및 출력
Sum_sort()

#평균이 80점 이상인 학생 수 계산 및 출력
Count_avg_over()

#탐색함수 호출
Research()

#모든 학생 정보 삭제(객체 삭제)
Remove(a,b,c,d,e)