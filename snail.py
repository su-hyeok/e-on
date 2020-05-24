matrix = int(input("수를 입력하세요:"))
data = [[0] * matrix for i in range(matrix)] 

horizonal = 0 
normal = -1 
listnumber = 0 
path = 1 

def snail(horizonal,normal,listnumber,path,matrix): 
    if matrix == 0 : 
        return 0 
    for p in range(1,matrix + 1): 
        listnumber = listnumber + 1 
        normal = normal + path 
        data[horizonal][normal] = listnumber  
    matrix = matrix - 1  
    for p in range(1,matrix + 1): 
        listnumber = listnumber + 1 
        horizonal = horizonal + path 
        data[horizonal][normal] = listnumber     
    path = path * -1
    return snail(horizonal,normal,listnumber,path,matrix)


snail(horizonal,normal,listnumber,path,matrix)
for horizonal in range(matrix):
    print(data[horizonal])
    