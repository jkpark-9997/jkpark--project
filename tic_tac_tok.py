# 성명 : 박재광 
# 학번: 2022078017 
# 프로그램 작성일시 : 2025-03-28 18:00
# 틱택톡 게임 만들기 프로젝트 과제

#게임 규칙 : 1. 상대방은 컴퓨터이며 컴퓨터는 다음 빈칸에 O를 놓는다. 2. 만약 플레이어가 더 이상 놓을 공간이 없을 경우 무승부로 처리한다.
#          3. 게임 크기는 3X3 크기이며, 사용자가 먼저 수를 놓는다. 4. 틱택톡 게임 규칙에 맞게 어떤 방향이든 일직선상의 동일한 수를 놓을 경우 '승리' 한다. 

#Copyringt chatgpt - check_win함수 로직을 명확하게 하는데 도움을 받음.

#게임 판을 2차원 리스트를 이용하영 생성(리스트 안의 리스트)
board = [[' ' for x in range(3)] for y in range(3)]

#승리 조건 체크 후 만족할 시 승리한 문자 반환(X or O), 아닐 경우 None 반환.
def check_win():
    #승리 조건1 : 동일한 행에 전부 같은 문자가 저장되어 있을 경우
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != ' '):
            return board[row][0]
    #승리 조건2 : 동일한 열에 전부 같은 문자가 저장되어 있는 경우
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != ' '):
            return board[0][col]
    #승리 조건3 : 대각선 방향의 인덱스의 요소에 전부 같은 문자가 저장되어 있는 경우
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != ' '):
        return board[0][0]
    #승리 조건4 : 역대각선 방향의 인덱스의 요소에 전부 같은 문자가 저장되어 있는 경우
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != ' '):
        return board[0][2]
    return None

#보드가 Full인지 확인하는 함수. (Full일 경우 무승부임을 판정하기 위한 함수.)
def check_Full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':#보드에 빈칸이 하나라도 있으면 Full이 아니므로 즉시, False 반환.
                return False
    return True#모든 보드를 확인한 결과 빈칸이 없을 경우 True반환->Full인 경우


while True:
    #게임 시작 전 초기화된 보드를 보여주기.
    for row in range(3):
        print(" ",board[row][0]," | ",board[row][1]," | ",board[row][2])
        if row < 2:
            print("-----|-----|-----")
    #while문 반복 하는과정에서 다시 보드에 수를 놓기전에 승리 or 무승부의 조건이 만족했는지 확인하기위해 승리체크함수와 무승부체크 함수를 호출
    Player = check_win()
    if Player:
        print("{0}를 사용한 플레이어 승리!".format(Player))
        break
    if check_Full():
        print("보드가 꽉찰 동안 승패가 안 났으므로 무승부!")
        break
    
    #보드의 좌표에 맞게 수 입력.
    x = int(input("다음 수의 x좌표를 입력하시오 (0~2): "))
    y = int(input("다음 수의 y좌표를 입력하시오 (0~2): "))
    if x not in range(3) or y not in range(3):
        print("잘못된 입력입니다. 0~2 사이의 숫자를 입력하세요.")
        continue#수를 잘못입력하였으니 다시 입력하기 위해 continue 활용.
    
    #잘못된 위치에 입력하였는지 확인(이미 수를 놓은 위치에는 다시 놓지 못함.)
    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue#수를 잘못입력하였으니 다시 입력하기 위해 continue 활용.
    else:#문제 없이 수 입력하였을 경우 보드에 추가.
        board[x][y] = 'X'
    
    #수로 놓은 후에 승패가 났는지 확인하기 위해 다시 한번 승리체크 함수 호출
    Player = check_win()
    if Player:#승패가 결정되어 Player가 None이 아닌경우
        for row in range(3):#반복문을 통해 수를 놓은 후의 보드 판을 보여 준후 승리한 플레이어 출력.
            print(" ",board[row][0]," | ",board[row][1]," | ",board[row][2])
            if row < 2:#3X3칸 보드 이기때문에 row의 값이 2인경우 더 이상 행을 구분할 필요 없음.
                print("-----|-----|-----")
        print("{0}를 사용한 플레이어 승리!".format(Player))
        break
    if check_Full():
        print("보드가 꽉찰 동안 승부가 안 났으므로 무승부!")
        break
    #아직 승부가 안났을 경우 다음 턴인 컴퓨터(상대 플레이어)가 수를 놓는다.
    done = False#프로그램상 위에서 break를 만나면 프로그램이 종료되기 때문에 불필요하지만 아직 게임이 종료되지 않았다는 의미를 넣기 위해 선언 및 초기화.
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:#반복문을 통해 보드상의 빈칸을 찾기
                board[i][j] = 'O'#찾은 경우 상대 플레이어 수인 'O'문자 대입.
                done = True
                break#수를 놓았으므로 상대 턴이니 반복문 빠져나오기.