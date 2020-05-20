#기차 예매 프로그램
import numpy as np
import datetime

class reservation:      #시간 출발역 도착역 열차종류
    def __init__(self):
        self.time = []      # 입력받은 시간
        self.time_temp = None  # 입력받은 시간을 시간값으로 변경
        self.time_list_temp = None # 원하는 조건에 해당하는 시간들
        self.result_list_temp = [] # 조건에 해당하는 값들 중 가장 가까운 값을 구할 때 사용할 리스트
        self.result_up_list_temp = [] # 입력받은 시간보다 낮은값이 가장 가까울 경우 높은값중 가장 가까운 값을 구할 때 사용할 리스트
        self.result_down_list_temp = [] # 입력받은 시간보다 높은값이 가장 가까울 경우 낮은값중 가장 가까운 값을 구할 때 사용할 리스트
        self.start = None # 출발역 입력
        self.arrive =None # 도착역 입력
        self.kind = None # 열차종류 입력
        self.f = None # 기차정보
        self.line = None # 기차정보를 저장한 값
        self.idx = None # 가장 가까운 값이 몇번째 줄인지 나타내는 수
        self.idx_down = None # 낮은 값중 가장 가까운 값의 줄
        self.idx_up = None # 높은 값중 가장 가까운 값의 줄
        self.line_1_temp = None # 가장 가까운 값이 몇번째 줄인지 나타내는 수를 저장하는 값
        self.line_2_temp = None # 2번째로 가까운 값을 저장
        self.updown_temp = None # 2번째로 가까운 값을 구하기 위한 조건에 해당하는 값들의 리스트
        self.listplz = None # 선택한 기차표의 좌석을 계산할 때 사용
        self.listplz2 = None # 선택한 기차표를 보기좋게 출력하기 위한 공간
        self.nono = None # 취소 선택지
        self.lines = None # 기차정보를 저장할 공간

    def train(self): # 1번 입력 함수
        while True:
            try:
                self.time = str(input("시간을 입력하세요  (ex) 08:00) :"))
                self.time_temp = datetime.datetime.strptime(self.time, '%H:%M')
                self.start= str(input("출발역을 입력하세요: "))
                self.arrive = str(input("도착역을 입력하세요: "))
                self.kind = str(input("열차종류를 입력하세요: "))
                print("{} {} -> {} {}".format(self.time,self.start,self.arrive,self.kind))
                break
            except:
                print("다시 입력하세요")
        
    def openit(self,f): # 시간비교
        self.line = f.readlines()
        for i in range(1,21):                   #선택한 시간과 가장 가까운 시간의 기차표를 구하는 함수
            str(self.line[i]).split()
            self.time_list_temp = datetime.datetime.strptime(self.line[i].split()[0], '%H:%M')
            if self.start == str(self.line[i]).split()[1] and self.arrive == str(self.line[i]).split()[3] and self.kind == str(self.line[i]).split()[4]:
                self.result_list_temp.append(self.time_list_temp)

        for i in range(1,21):
            str(self.line[i]).split()
            self.time_list_temp = datetime.datetime.strptime(self.line[i].split()[0], '%H:%M')

            if self.start == str(self.line[i]).split()[1] and self.arrive == str(self.line[i]).split()[3] and self.kind == str(self.line[i]).split()[4]:
                self.result_list_temp = np.asarray(self.result_list_temp)
                self.idx = (np.abs(self.result_list_temp - self.time_temp)).argmin()

                if self.result_list_temp[self.idx] == self.time_list_temp:
                    print(self.line[i])
                    self.line_1_temp = i

        if self.result_list_temp[self.idx] < self.time_temp:

            for i in range(self.line_1_temp+1,21):                   #선택한 시간과 두번째로 가까운 시간의 기차표를 구하는 함수
                str(self.line[i]).split()
                self.time_list_temp = datetime.datetime.strptime(self.line[i].split()[0], '%H:%M')

                if self.start == str(self.line[i]).split()[1] and self.arrive == str(self.line[i]).split()[3] and self.kind == str(self.line[i]).split()[4]:
                    self.result_up_list_temp.append(self.time_list_temp)

            for l in range(self.line_1_temp+1,21):
                str(self.line[l]).split()
                self.time_list_temp = datetime.datetime.strptime(self.line[l].split()[0], '%H:%M')

                if self.start == str(self.line[l]).split()[1] and self.arrive == str(self.line[l]).split()[3] and self.kind == str(self.line[l]).split()[4]:
                    self.result_up_list_temp = np.asarray(self.result_up_list_temp)
                    self.idx_up = (np.abs(self.result_up_list_temp - self.time_temp)).argmin()

                    if self.result_up_list_temp[self.idx_up] == self.time_list_temp:
                        print(self.line[l])
                        self.line_2_temp = l

        elif self.result_list_temp[self.idx] > self.time_temp:

            for i in range(1,self.line_1_temp-1):                   #선택한 시간과 두번째로 가까운 시간의 기차표를 구하는 함수
                str(self.line[i]).split()
                self.time_list_temp = datetime.datetime.strptime(self.line[i].split()[0], '%H:%M')

                if self.start == str(self.line[i]).split()[1] and self.arrive == str(self.line[i]).split()[3] and self.kind == str(self.line[i]).split()[4]:
                    self.result_down_list_temp.append(self.time_list_temp)

            for l in range(1,self.line_1_temp-1):
                str(self.line[l]).split()
                self.time_list_temp = datetime.datetime.strptime(self.line[l].split()[0], '%H:%M')

                if self.start == str(self.line[l]).split()[1] and self.arrive == str(self.line[l]).split()[3] and self.kind == str(self.line[l]).split()[4]:
                    self.result_down_list_temp = np.asarray(self.result_down_list_temp)
                    self.idx_down = (np.abs(self.result_down_list_temp - self.time_temp)).argmin()

                    if self.result_down_list_temp[self.idx_down] == self.time_list_temp:
                        print(self.line[l])
                        self.line_2_temp = l
        

    def choose(self): # 위에꺼 예약
        self.listplz = []
        self.listplz = self.line[self.line_1_temp].split()
        if int(self.listplz[5]) == 0:
            print("매진이어서 예약할 수 없습니다.")
        else:
            print("예약 완료")
            self.listplz[5] = str(int(self.listplz[5]) - 1)
            self.listplz2 = " ".join(self.listplz)
            print(self.listplz2)
            return (self.line_1_temp,self.listplz2)
        return self.listplz2

    def temp1(self):
        return self.listplz

    def choose2(self): # 아래꺼 예약
        self.listplz = []
        self.listplz = self.line[self.line_2_temp].split()
        if int(self.listplz[5]) == 0:
            print("매진이어서 예약할 수 없습니다.")
        else:
            print("예약 완료")
            self.listplz[5] = str(int(self.listplz[5]) - 1)
            self.listplz2 = " ".join(self.listplz)
            print(self.listplz2)
            return (self.line_2_temp,self.listplz2)
        return self.listplz2

    def temp2(self):
        return self.listplz


    def confirm(self,listplz2,listplz): # 예매 취소
        while True:
            self.nono = int(input("취소하시겠습니까(예1,아니오2,뒤로가기3): "))
            if self.nono == 1:
                print("예매를 취소합니다")
                listplz[5] = str(int(listplz[5]) + 1) 
                listplz2 = " ".join(listplz)
                print(listplz2)
                return listplz2
                break
            elif self.nono == 2:
                break
            elif self.nono == 3:
                break
            else:
                print("1~2 사이의 값을 입력하세요")

    def check1(self,listplz2): # 예매현황 보여주기(1번경우)
        print("예약 현황입니다.")
        print(listplz2[1])

    def check2(self,listplz2): # 예매현황 보여주기(2번경우)
        print("예약 현황입니다.")
        print(listplz2[1])
            

                    
    def whole(self,f): # 기차정보 보여주기
        self.lines = []
        self.lines = f.read()
        print(self.lines)


while(True):
    vari1 = int(input("메뉴를 입력해수세요(1:예약, 2:기차정보, 3:예매현황 및 취소, 4:프로그램 종료): ")) # 메인 메뉴
    f = open("C:/Users/이수혁/Desktop/TrainList.txt",'r')
    a = reservation()
    if vari1 == 4:
        print("프로그램 종료")
        break
    if vari1 == 1:
        a.train()
        a.openit(f)
        while True:
            dothis = int(input("위에꺼 예약1,아래꺼 예약2,뒤로가기3: "))
            if dothis == 1:
                temp = a.choose()
                list_temp = a.temp1()
                break
            elif dothis == 2:
                temp = a.choose2()
                list_temp = a.temp2()
                break
            elif dothis == 3:
                break
            else:
                print("1~3사이의 값을 입력하세요")
    elif vari1 == 2:
        a.whole(f)
        break
    elif vari1 == 3:
        while True:
            thatnono = int(input("예약 현황을 확인하시겠습니까? 1 확인, 2 뒤로가기"))
            if thatnono == 1:
                if dothis == 1:
                    a.check1(temp)
                    temp = a.confirm(temp,list_temp)
                    break
                elif dothis == 2:
                    a.check2(temp)
                    temp = a.confirm(temp,list_temp)
                    break
            elif thatnono == 2:
                break
            else:
                print("1~2사이의 값을 입력하세요")
            break
    else:
        print("1~4 사이의 값을 입력하여 주세요")
        break