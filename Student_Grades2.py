# 성명 : 박재광 
# 학번: 2022078017 
# 프로그램 작성일시 : 2025-03-22 17:00
# 성적관리 프로그램(함수) 만들기 개인과제

#키보드로부터 학번, 이름, 영어점수, C-언어점수, 파이썬 점수를 입력받아 총점,평균,등수를 계산하는 프로그램작성
#학점을 평균을 근거로 하며, 과락점수는 60점 미만으로 한다.


#학생별 총점 및 평균 계산 함수( 두 개의 반환 값을 전달)
def sum_average_score(a,b,c):
    sum=(a+b+c)#총점
    average=(int)(sum/3)#평균
    return sum,average

#학생별 평균을 근거로한 학점 계산 함수
def grade_student(arr):
    grade=[]#학생 별 학점을 저장할 리스트 생성
    for i in range(5):#반복문을 통해 학생별 평균을 근거로 학점을 리스트에 저장.
     if arr[i] >=95:
        grade.append("A+")
     elif arr[i]>=90 and arr[i]<95:
        grade.append("A0")
        
     elif arr[i]>=85 and arr[i]<90:
        grade.append("B+")
        
     elif arr[i]<85 and arr[i]>=80:
        grade.append("B0")
        
     elif arr[i]<80 and arr[i]>=75:
        grade.append("C+")
        
     elif arr[i]<75 and arr[i]>=70:
        grade.append("C0")
        
     elif arr[i]<70 and arr[i]>=65:
        grade.append("D+")
        
     elif arr[i]<65 and arr[i]>=60:
        grade.append("D0")
        
     else:
        grade.append("F")
    return grade# 학점이 저장된 리스트 반환


#학생별 평균점수에 따른 등수 계산 함수(딕셔너리 활용)
def Rank_score(ary):
   rank_score = {}
#내림차순 정렬돼있으므로, 반복문을 통해 순서대로 등수(rank)부여
   rank = 1
   for score in ary:
    if score not in rank_score:  # 점수가 딕셔너리에 저장되어있지 않을 시 등수저장.(중복을 피하기위해 동일한 점수가 이미 있는 경우 저장하지 않고 유지)
        rank_score[score] = rank
    rank += 1  # 다음 등수를 증가시킴
   return rank_score


#학생별 학번,이름,과목별 점수, 총점, 평균, 학점, 등수 출력 함수
def Studnet_grade_print(num,name,a,b,c,d,e,a_sum,b_sum,c_sum,d_sum,e_sum,arr,Grade,rank_score):
   print("                  성적관리 프로그램               \n")
   print("================================================================\n")
   print("학번      이름        영어  C-언어  파이썬  총점  평균  학점  등수\n")
   print("================================================================\n")
   print(num[0],name[0],"   ",a[0],"   ",a[1],"   ",a[2],"   ",a_sum,"   ",arr[0],"   ",Grade[0],"   ",rank_score[arr[0]],"\n")
   print(num[1],name[1],"   ",b[0],"   ",b[1],"   ",b[2],"   ",b_sum,"   ",arr[1],"   ",Grade[1],"   ",rank_score[arr[1]],"\n")
   print(num[2],name[2],"   ",c[0],"   ",c[1],"   ",c[2],"   ",c_sum,"   ",arr[2],"   ",Grade[2],"   ",rank_score[arr[2]],"\n")
   print(num[3],name[3],"   ",d[0],"   ",d[1],"   ",d[2],"   ",d_sum,"   ",arr[3],"   ",Grade[3],"   ",rank_score[arr[3]],"\n")
   print(num[4],name[4],"   ",e[0],"   ",e[1],"   ",e[2],"   ",e_sum,"   ",arr[4],"   ",Grade[4],"   ",rank_score[arr[4]],"\n")

#학번와 이름을 저장할 리스트 생성
student_num=[]
student_name=[]

#5명의 학생의 학번과 이름 입력받아 리스트에 저장하기.
for i in range(5):
   student_num.append((int)(input("학생{0}의 학번을 입력하시오.".format(i+1))))
   student_name.append((input("학생{0}의 이름을 입력하시오.".format(i+1))))

#학생1의 점수를 입력받음
a=[]
a.append((int)(input("학생1의 영어 점수를 입력하시오.")))
a.append((int)(input("학생1의 C-언어 점수를 입력하시오.")))
a.append((int)(input("학생1의 파이썬 점수를 입력하시오.")))

#학생2의 점수를 입력받음
b=[]
b.append((int)(input("학생2의 영어 점수를 입력하시오.")))
b.append((int)(input("학생2의 C-언어 점수를 입력하시오.")))
b.append((int)(input("학생2의 파이썬 점수를 입력하시오.")))

#학생3의 점수를 입력받음
c=[]
c.append((int)(input("학생3의 영어 점수를 입력하시오.")))
c.append((int)(input("학생3의 C-언어 점수를 입력하시오.")))
c.append((int)(input("학생3의 파이썬 점수를 입력하시오.")))

#학생4의 점수를 입력받음
d=[]
d.append((int)(input("학생4의 영어 점수를 입력하시오.")))
d.append((int)(input("학생4의 C-언어 점수를 입력하시오.")))
d.append((int)(input("학생4의 파이썬 점수를 입력하시오.")))

#학생5의 점수를 입력받음
e=[]
e.append((int)(input("학생5의 영어 점수를 입력하시오.")))
e.append((int)(input("학생5의 C-언어 점수를 입력하시오.")))
e.append((int)(input("학생5의 파이썬 점수를 입력하시오.")))

#학생별 총점과 평균을 함수를 호출하여 반환값을 전달받아 각각의 변수에 저장(반환값이 두개 이므로 각각 두개의 변수 생성)
a_sum ,a_average = sum_average_score(a[0],a[1],a[2])#학생1의 총점, 평균
b_sum ,b_average= sum_average_score(b[0],b[1],b[2])#학생2의 총점, 평균
c_sum ,c_average= sum_average_score(c[0],c[1],c[2])#학생3의 총점, 평균
d_sum ,d_average = sum_average_score(d[0],d[1],d[2])#학생4의 총점, 평균
e_sum ,e_average= sum_average_score(e[0],e[1],e[2])#학생5의 총점, 평균

arr = []#학점을 구하기위한 반복문을 돌리기 위해 학생들의 평균을 리스트에 저장
arr.append(a_average)
arr.append(b_average)
arr.append(c_average)
arr.append(d_average)
arr.append(e_average)


Grade=[]
Grade=grade_student(arr)#학생별 평균을 근거로한 학점을 반환하여 리스트에 저장.


ary=arr[:]#등수를 따지기위해 리스트를 내림차순 정렬할 것이므로, 기존 리스트의 변경을 막기위해 복사
for i in range(4):#복사한 리스트를 활용하여 내림차순 정렬-> 평균이 높은 순서대로 앞쪽에 배치될 것임.
    max=i
    for j in range(i+1,5):
        if ary[j]>=ary[max]:
            max=j
    ary[i],ary[max]=ary[max],ary[i]
    

#등수 계산 함수를 호출하여 점수와 등수가 key, value로써 저장된 딕셔너리를 생성한 후 반환하여 객체에 저장.
rank_score = Rank_score(ary)

#출력함수 호출.
Studnet_grade_print(student_num,student_name,a,b,c,d,e,a_sum,b_sum,c_sum,d_sum,e_sum,arr,Grade,rank_score)


