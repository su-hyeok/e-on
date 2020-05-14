number  = int(input("작업의  개수 입력: "))
pick = int(input("출력할 작업 입력: "))
rank = list(map(int,input("우선순위 입력: ").split()))


def sort1(rank1 , pick1):

    list1 = [c for c in range(len(rank1))]
    list2 = rank1.copy() 

    i = 0
    while True:
        if list2[i] < max(list2[i:]):
            list1.append(list1.pop(i))
            list2.append(list2.pop(i))
        
            
        else:
            i += 1
            

        if list2 == sorted(list2, reverse=True):
            break

    return list1.index(pick1) + 1

print("{}분".format(sort1(rank,pick)))

