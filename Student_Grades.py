#학생1,2,3,4,5 는 5명의 학생이다. 각각 과목별 점수를 갖는다.
#과목별 최소 부여 점수는 60점이다.따라서 점수를 부여했다면 최소 D학점은 나오고,시험 미응시의 경우 10점으로 취급해서 F가 부여된다.
#등수는 평균을 이용해서 나눈다. 같을 경우 같은 등수로 한다.


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

#학생별 총점을 구하고,총점을 3으로 나눠 평균을 구함
a_sum=a[0]+a[1]+a[2]#학생1의 총점
b_sum=b[0]+b[1]+b[2]#학생2의 총점
c_sum=c[0]+c[1]+c[2]#학생3의 총점
d_sum=d[0]+d[1]+d[2]#학생4의 총점
e_sum=e[0]+e[1]+e[2]#학생5의 총점

print("학생1의 총점 : ",a_sum)
print("학생2의 총점 : ",b_sum)
print("학생3의 총점 : ",c_sum)
print("학생4의 총점 : ",d_sum)
print("학생5의 총점 : ",e_sum)

print("학생1의 평균 점수 : ",a_sum//3)
print("학생2의 평균 점수 : ",b_sum//3)
print("학생3의 평균 점수 : ",c_sum//3)
print("학생4의 평균 점수 : ",d_sum//3)
print("학생5의 평균 점수 : ",e_sum//3)

arr = []#학점을 구하기위한 반복문을 돌리기 위해 학생들의 평균을 리스트에 저장
arr.append(a_sum//3)
arr.append(b_sum//3)
arr.append(c_sum//3)
arr.append(d_sum//3)
arr.append(e_sum//3)


for i in range(5):#반복문을 통해 학생별 평균을 근거로 학점을 부여
    if arr[i] >=90:
        print("학생",i+1,"학점 : A")
    elif arr[i]<90 and arr[i]>=80:
        print("학생",i+1,"학점 : B")
    elif arr[i]<80 and arr[i]>=70:
        print("학생",i+1,"학점 : C")
    elif arr[i]<70 and arr[i]>=60:
        print("학생",i+1,"학점 : D")
    else:
        print("학생",i+1,"학점 : F")


ary=arr[:]#등수를 따지기위해 리스트를 내림차순 정렬할 것이므로, 기존 리스트의 변경을 막기위해 복사
for i in range(4):#복사한 리스트를 활용하여 내림차순 정렬-> 평균이 높은 순서대로 앞쪽에 배치될 것임.
    max=i
    for j in range(i+1,5):
        if ary[j]>=ary[max]:
            max=j
    ary[i],ary[max]=ary[max],ary[i]
    

# 등수를 매기기 위해 딕셔너리 활용
rank_score = {}
#내림차순 정렬돼있으므로, 반복문을 통해 순서대로 등수(rank)부여
rank = 1
for score in ary:
    if score not in rank_score:  # 점수가 딕셔너리에 저장되어있지 않을 시 등수저장.(중복을 피하기위해 동일한 점수가 이미 있는 경우 저장하지 않고 유지)
        rank_score[score] = rank
    rank += 1  # 다음 등수를 증가시킴


for i in range(5):
    score = arr[i]  # 기존의 리스트에 저장되어 있던 학생의 평균점수 활용하여 딕셔너리에 접근해 등수 가져오기.
    print("학생",i+1,"등수 : ",rank_score[score],"등 (평균:",score,")")


