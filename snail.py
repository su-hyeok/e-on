matrix = int(input("수를 입력하세요:"))
data = [[0] * matrix for i in range(matrix)] 

horizonal = 0 
normal = -1 
listnumber = 0 
path = 1 
inputnum = matrix 

def snail(horizonal,normal,listnumber,path,inputnum): 
    if inputnum == 0 : 
        return 0 
    for p in range(1,inputnum+1): 
        listnumber = listnumber + 1 
        normal = normal + path 
        data[horizonal][normal] = listnumber  
    inputnum = inputnum - 1  
    for p in range(1,inputnum+1): 
        listnumber = listnumber + 1 
        horizonal = horizonal + path 
        data[horizonal][normal] = listnumber     
    path = path * -1
    return snail(horizonal,normal,listnumber,path,inputnum)


snail(horizonal,normal,listnumber,path,inputnum)
for horizonal in range(matrix):
    print(data[horizonal])
    