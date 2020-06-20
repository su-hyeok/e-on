from db import database
import numpy as np
import db
class application:
    def __init__(self,filepath):
        self.text = database(filepath)
        self.menu()
    def add(self):
        self.bookname = input("추가할 도서명을 입력하세요: ")
        self.author = input("추가할 저자를 입력하세요: ")
        self.published = input("추가할 출판년도를 입력하세요: ")
        self.publisher = input("추가할 출판사명을 입력하세요: ")
        self.genre = input("장르를 입력하세요: ")
        self.text.DB = np.append(self.text.DB, [[self.bookname,self.author,self.published,self.publisher,self.genre]], axis=0)
        print(self.text.DB)

    def sub(self):
        print("""
        ==================
        1.도서명으로 검색
        2.저자로 검색
        3.출판년도로 검색
        4.출판사명으로 검색
        5.장르로 검색
        ===================""")
        self.option = int(input("검색할 메뉴를 선택하세요: "))
        if self.option == 1:
            self.bookname = input("도서명을 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.title)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.bookname],axis = 0)
                self.b = np.append(self.list1, [self.array[i][0]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])
                
        elif self.option == 2:
            self.author = input("저자를 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.authors)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.author],axis = 0)
                self.b = np.append(self.list1, [self.array[i][1]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])
        elif self.option == 3:
            self.published = input("출판년도를 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.published)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.published],axis = 0)
                self.b = np.append(self.list1, [self.array[i][2]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])
        elif self.option == 4:
            self.publisher = input("출판사명을 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.publisher)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.publisher],axis = 0)
                self.b = np.append(self.list1, [self.array[i][3]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])
        elif self.option == 5:
            self.genre = input("장르를 입력하세요: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.genre)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.genre],axis = 0)
                self.b = np.append(self.list1, [self.array[i][4]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])

    def modify(self):

        print(self.array)
        self.change = int(input("수정할 번째를 입력하세요,0은 도서명,1은 저자: "))
        if self.change == 0:
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))    
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][0] = self.name
                    print(self.text.DB[i])
        elif self.change == 1:
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))    
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][1] = self.name
                    print(self.text.DB[i])
        elif self.change == 2:
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))    
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][2] = self.name
                    print(self.text.DB[i])
        elif self.change == 3:
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))    
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][3] = self.name
                    print(self.text.DB[i])
        elif self.change == 4:
            self.num = int(input("수정할 번째를 입력하세요(0은 제일 위 ):"))    
            self.name = input("수정할 내용을입력하세요: ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][4] = self.name
                    print(self.text.DB[i])
    def delete(self):
        print(self.array)
        self.tt = int(input("삭제할 번째를 입력하세요(위에서부터 0번째):"))
        for i in range(len(self.text.DB)):
            if i == self.tt:
               self.d = np.delete(self.array,(i),axis = 0)
               self.array = self.d
               print(self.array)
    def show(self):
        print(self.d)
    def save(self):
        np.save("C:/Users/이수혁/Desktop/1.txt",self.text.DB)
        self.saveload = np.load("C:/Users/이수혁/Desktop/1.txt.npy")
        print(self.saveload)


    def menu(self):
        self.array = np.array(self.text.DB,str)
        print("""
    ==================
    1.도서 추가
    2.도서 검색
    3.도서 정보 수정
    4.도서 삭제
    5.현재 총 도서 목록
    6.저장
    7.나가기
    ===================""")
        self.option = int(input("메뉴를 선택하세요: "))
        if self.option == 1:
           self.add()
           self.menu()
        elif self.option == 2:
            self.sub()
            self.menu()
        elif self.option == 3:
            self.modify()
            self.menu()
        elif self.option == 4:
            self.delete()
            self.menu()
        elif self.option == 5:
            self.show()
            self.menu()
        elif self.option == 6:
            self.save()
            self.menu()
        elif self.option == 7:
            self.save()


if __name__ =="__main__":
    app = application("input.txt")