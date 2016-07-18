
def OpenFileTxt(FileAddress):

    OpenedFile = open(FileAddress, 'r')

    OpenedFile = [x.strip() for x in OpenedFile if x.strip()]

    OpenedFile = [int(i) for i in OpenedFile]

    return OpenedFile

def SortANDCount (ArrayToBeSorted):
    # print()
    # print('SortANDCount')
    ArrayLen=len(ArrayToBeSorted)
    # print('ArrayLen=', ArrayLen)
    # print('ArrayToBeSorted=',ArrayToBeSorted)


    if ArrayLen == 1 or ArrayLen == 0:
        # print('Returning ArrayToBeSorted (', [ArrayToBeSorted,0],')')
        return [ArrayToBeSorted,0]
    else:
        # print('ArrayLen//2=',ArrayLen//2)
        # print('Recursion 1 with list ', ArrayToBeSorted[0:ArrayLen//2])
        LeftHalf=SortANDCount(ArrayToBeSorted[0:ArrayLen//2])
        # print()
        # print('Recursion 2 with list ', ArrayToBeSorted[ArrayLen // 2:ArrayLen])
        RightHalf=SortANDCount(ArrayToBeSorted[ArrayLen // 2:ArrayLen])

        # print('LeftHalf[0]',LeftHalf[0])
        # print('RightHalf[0]',RightHalf[0])

        MergedList=Merg_AND_CountSplitInv(LeftHalf[0],RightHalf[0])

        # print()
        # print('MergedList',MergedList)
        # print('RightHalf',RightHalf)
        # print('LeftHalf', LeftHalf)
        X = LeftHalf[1]
        Y = RightHalf[1]
        Z = MergedList[1]

        # print()
        # print('X,Y,Z = ',X,' ',Y,' ',Z )
        return MergedList[0], X+Y+Z

def Merg_AND_CountSplitInv (LeftHalf, RightHalf):

    # print()
    # print('Merg_AND_CountSplitInv')
    numLeft=0
    numRight=0
    MergedList=[]
    Inversions=0

    for num in range(0, len(LeftHalf)+len(RightHalf)):

        # print('LeftHalf',LeftHalf)
        # print('RightHalf',RightHalf)
        # print('numLeft',numLeft)
        # print('numRight',numRight)
        # print('LeftHalf[numLeft]', LeftHalf[numLeft])
        # print('RightHalf[numRight]', RightHalf[numRight])
        # print('MergedList', MergedList)

        if numLeft >= len(LeftHalf) and numRight <= len(RightHalf): #If True, it means that all itens from the LeftHalf were checked
            # print()
            # print('RightHalf[numRight]',RightHalf[numRight])
            # print('Merged list before append=',MergedList)
            MergedList.append(RightHalf[numRight])
            # print('1 - numLeft > len(LeftHalf) and numRight < len(RightHalf)=',
            #       numLeft > len(LeftHalf) and numRight < len(RightHalf))
            # print('Merged list after append=', MergedList)
            numRight += 1
        elif numRight >= len(RightHalf) and numLeft < len(LeftHalf): #If True, it means that all itens from the RightHalf were checked
            # print()
            # print('LeftHalf[numLeft]',LeftHalf[numLeft])
            # print('Merged list before append=', MergedList)
            MergedList.append(LeftHalf[numLeft])
            # print('2 - numRight > len(RightHalf) and numLeft < len(LeftHalf)=',
            #       numRight > len(RightHalf) and numLeft < len(LeftHalf))
            # print('Merged list after append=', MergedList)
            numLeft += 1
        elif LeftHalf[numLeft] < RightHalf[numRight]: #There is a problem here because of the lenght of the lists
            # print()
            # print('RightHalf[numRight]', RightHalf[numRight])
            # print('LeftHalf[numLeft]',LeftHalf[numLeft])
            # print('Merged list before append=', MergedList)
            MergedList.append(LeftHalf[numLeft])
            # print('3 - LeftHalf[numLeft] < RightHalf[numRight]=', LeftHalf[numLeft] < RightHalf[numRight])
            # print('Merged list after append=', MergedList)
            numLeft += 1
        elif RightHalf[numRight] < LeftHalf[numLeft]:
            # print()
            # print('RightHalf[numRight]',RightHalf[numRight])
            # print('LeftHalf[numLeft]', LeftHalf[numLeft])
            # print('Merged list before append=', MergedList)
            MergedList.append(RightHalf[numRight])
            Inversions += len(LeftHalf)-numLeft # THIS DETAIL IS CRUCIAL! The number of inversions at this point is
            # equal to the number of itens left in the left array!!!
            # print('4 - RightHalf[numRight] < LeftHalf[numLeft]=', RightHalf[numRight] < LeftHalf[numLeft])
            # print('Merged list after append=', MergedList)
            numRight += 1

    # print('MergedList',MergedList)
    # print('Inversions',Inversions)
    return [MergedList,Inversions]

#Tests
AB1=[1,5,8,4,7,6,2,9]
AB2=[1,5]
AB3=[1,3,5,2,4,6]
AB4=[4,3,2,1]
AB5=[]
MergedLists1=SortANDCount(AB1)
MergedLists2=SortANDCount(AB2)
MergedLists3=SortANDCount(AB3)
MergedLists4=SortANDCount(AB4)
MergedLists5=SortANDCount(AB5)

print('MergedLists1',MergedLists1)
print('MergedLists2',MergedLists2)
print('MergedLists3',MergedLists3)
print('MergedLists4',MergedLists4)
print('MergedLists5',MergedLists5)

Text_File = 'D:\\UnB\\Cursos\\Coursera\\AlgorithmDesign\\ProgrammingAssigment_1_IntegerArray.txt'
NewList=OpenFileTxt(Text_File)
NewList_Inversions=SortANDCount(NewList)

print(NewList_Inversions[1])




#Some useful links or comments considered to create this algorithm
# http://www.secnetix.de/olli/Python/list_comprehensions.hawk
#https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
