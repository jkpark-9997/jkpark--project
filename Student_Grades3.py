# 성명 : 박재광 
# 학번: 2022078017 
# 프로그램 작성일시 : 2025-03-28 20:00
# 성적관리 프로그램(함수) 만들기 개인과제2(삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수 추가)

#키보드로부터 학번, 이름, 영어점수, C-언어점수, 파이썬 점수를 입력받아 총점,평균,등수를 계산하는 프로그램작성
#학점을 평균을 근거로 하며, 과락점수는 60점 미만으로 한다.

#총점과 평균 반환 함수
def sum_average_score(a):
    sum=(a[0]+a[1]+a[2])#총점
    average=(int)(sum/3)#평균
    return sum,average

# 평균 80점 이상 학생 수 카운트 함수
def average_eighty_up(arr):#과목별 평균을 저장한 리스트를 매개변수로 전달
   count=0
   for i in arr:#반복문을 돌려 리스트안의 저장된 값이 80이상 일시 카운트+1
      if(i>=80):
        count+=1

   return count

#총점 정렬 함수
def sort_sum(all_sum):
   all_sum.sort(reverse=True)#sort함수를 활용하여 총점이 저장된 리스트 내림차순으로 정렬
   print("학생 별 총점을 내림차순으로 정렬 : ")
   for i in range(len(all_sum)):
      print(all_sum[i])  

#학생별 평균을 근거로한 학점 계산 함수
def grade_student(arr):
    grade=[]#학생 별 학점을 저장할 리스트 생성
    for i in range(len(arr)):#반복문을 통해 학생별 평균을 근거로 학점을 리스트에 저장.(추가한 점 : 삽입함수 추가로 인해 범위를 리스트의 크기에 맞게 설정)
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


#새로운 학생 정보 저장(삽입함수)
def student_insert(num,name,scores,all_sum,arr,Grade):#매개변수로 기존의 리스트들을 전달
   num.append((int)(input("추가할 학생의 학번을 입력하시오.")))
   name.append((input("추가할 학생의 이름을 입력하시오.")))
   new_scores = list(map(int, input("추가할 학생의 영어, C-언어, 파이썬 점수: ").split()))#학생별 점수를 한번에 입력받아 split함수를 통해 공백으로 점수를 구분하고, map함수를 통해 정수로 변환하여 저장 리스트 저장.
   scores.append(new_scores)#리스트 안에 리스트 저장함으로써 학생별로 세 과목 점수를 묶어 저장.
   new_sum, new_average = sum_average_score(new_scores)  # 총점과 평균 계산
   all_sum.append(new_sum)#총점 리스트에 새로운 총점 추가
   arr.append(new_average)#평균 리스트에 새로운 평균 추가
   Grade=grade_student(arr)#학점 리스트는 리스트를 반환하므로 새로운 리스트에 덮어씌어 변경
   return Grade#변경된 리스트 반환


#학생의 학번을 이용한 정보 탐색(탐색함수)
def student_search(num, name, scores, all_sum, arr, grade):#매개변수로 학생들의 정보가 저장된 리스트 전달
    search_id = int(input("검색할 학생의 학번을 입력하시오: "))
    if search_id in num:#탐색할 학번이 리스트 안에 있을 경우에만 실행
        index = num.index(search_id)#탐색할 학번의 인덱스 값을 찾아 저장(탐색 키로 활용)
        print("학생 ",search_id,"의 정보:")
        print("이름: ",name[index])
        print("영어 점수: ",scores[index][0])
        print("C-언어 점수: ",scores[index][1])
        print("파이썬 점수: ",scores[index][2])
        print("총점: ",all_sum[index])
        print("평균: ",arr[index])
        print("학점: ",grade[index])
    else:
        print("해당 학번의 학생을 찾을 수 없습니다.")   

#학생의 학번을 이용한 정보 삭제(삭제함수)
def student_delete(num, name, scores, all_sum, arr, grade):#매개변수로 학생들의 정보가 저장된 리스트 전달
    delete_id = int(input("삭제할 학생의 학번을 입력하시오: "))
    if delete_id in num:
        index = num.index(delete_id)#삭제할 학번인 학생의 정보에 해당하는 인덱스 값을 저장(삭제 키로 활용)
        #pop함수를 활용하여 각각의 정보가 담긴 리스트 내의 데이터 삭제
        num.pop(index)
        name.pop(index)
        scores.pop(index)
        all_sum.pop(index)
        arr.pop(index)
        grade.pop(index)
        print(f"학번 {delete_id} 학생이 삭제되었습니다.")
    else:
        print("해당 학번의 학생을 찾을 수 없습니다.")   
   

#학생별 학번,이름,과목별 점수, 총점, 평균, 학점, 등수 출력 함수
def Studnet_grade_print(num,name,scores,sum,arr,Grade,rank_score):
   print("                  성적관리 프로그램               \n")
   print("================================================================\n")
   print("학번      이름        영어  C-언어  파이썬  총점  평균  학점  등수\n")
   print("================================================================\n")
   for i in range(len(num)):
    print(num[i],"   ",name[i],"   ",scores[i],"   ",sum[i],"   ",arr[i],"   ",Grade[i],"   ",rank_score[arr[i]],"\n")
   print("평균 80점 이상 학생 수 : ",average_eighty_up(arr))#평균 점수가 80점 이상인 학생의 수 출력

#학번와 이름을 저장할 리스트 생성
student_num=[]
student_name=[]
student_scores=[]
#5명의 학생의 학번과 이름 입력받아 리스트에 저장하기.
for i in range(5):
   student_num.append((int)(input("학생{0}의 학번을 입력하시오.".format(i+1))))
   student_name.append((input("학생{0}의 이름을 입력하시오.".format(i+1))))
   scores = list(map(int, input("학생 {0}의 영어, C-언어, 파이썬 점수: ".format(i+1)).split()))#학생별 점수를 한번에 입력받아 split함수를 통해 공백으로 점수를 구분하고, map함수를 통해 정수로 변환하여 저장 리스트 저장.
   student_scores.append(scores)#리스트 안에 리스트 저장함으로써 학생별로 세 과목 점수를 묶어 저장.


#학생별 총점과 평균을 함수를 호출하여 반환값을 전달받아 각각의 변수에 저장(반환값이 두개 이므로 각각 두개의 변수 생성)
a_sum ,a_average = sum_average_score(student_scores[0])#학생1의 총점, 평균
b_sum ,b_average= sum_average_score(student_scores[1])#학생2의 총점, 평균
c_sum ,c_average= sum_average_score(student_scores[2])#학생3의 총점, 평균
d_sum ,d_average = sum_average_score(student_scores[3])#학생4의 총점, 평균
e_sum ,e_average= sum_average_score(student_scores[4])#학생5의 총점, 평균

all_sum=[a_sum,b_sum,c_sum,d_sum,e_sum]#학생들의 총점을 리스트로 저장

arr = []#학점을 구하기위한 반복문을 돌리기 위해 학생들의 평균을 리스트에 저장
arr.append(a_average)
arr.append(b_average)
arr.append(c_average)
arr.append(d_average)
arr.append(e_average)


Grade=[]
Grade=grade_student(arr)#학생별 평균을 근거로한 학점을 반환하여 리스트에 저장.


ary=arr[:]#등수를 따지기위해 리스트를 내림차순 정렬할 것이므로, 기존 리스트의 변경을 막기위해 복사
for i in range(len(ary)):#복사한 리스트를 활용하여 내림차순 정렬-> 평균이 높은 순서대로 앞쪽에 배치될 것임.
    ary.sort(reverse=True)#sort함수 활용
    

#등수 계산 함수를 호출하여 점수와 등수가 key, value로써 저장된 딕셔너리를 생성한 후 반환하여 객체에 저장.
rank_score = Rank_score(ary)

#출력함수 호출.
Studnet_grade_print(student_num,student_name,student_scores,all_sum,arr,Grade,rank_score)

#새로운 학생 추가를 위한 메뉴 실행 반복문
while True:
    print("[1]삽입 [2]삭제 [3]탐색 [4]총점 정렬 [5]종료")
    menu = int(input())
    if menu == 1:
        Grade=student_insert(student_num, student_name, student_scores, all_sum, arr, Grade)#삽입함수
        ary = arr[:]  # 새롭게 등수를 따지기 위해 리스트를 내림차순 정렬할 것이므로, 새로운 학생이 추간된 원본 리스트의 변경을 막기 위해 복사
        ary.sort(reverse=True)#sort함수를 활용한 내림차순 정렬
        rank_score = Rank_score(ary)#등수 계산 함수호출
        #학생이 추가됐으므로 확인을 위해 전체학생 정보 출력.
        Studnet_grade_print(student_num, student_name, student_scores, all_sum, arr, Grade, rank_score)

    elif menu == 2:
        student_delete(student_num, student_name, student_scores, all_sum, arr, Grade)#삭제함수
        ary = arr[:]
        ary.sort(reverse=True)
        rank_score = Rank_score(ary)#학생이 삭제됐으므로 등수의 변동이 있을 것이므로 등수계산 함수 다시 호출
        #학생이 삭제됐으므로 확인을 위해 전체학생 정보 출력.
        Studnet_grade_print(student_num, student_name, student_scores, all_sum, arr, Grade, rank_score)

    elif menu == 3:
        student_search(student_num, student_name, student_scores, all_sum, arr, Grade)#탐색함수

    elif menu == 4:
        sort_sum(all_sum)#총점 정렬 함수

    elif menu == 5:#메뉴 선택 종료를 위한 반복문 탈출.
        break
    else:
        print("잘못된 값을 입력하셨습니다.")
#끝으로 최종 변경된 학생 전체 정보 출력
Studnet_grade_print(student_num,student_name,student_scores,all_sum,arr,Grade,rank_score)
