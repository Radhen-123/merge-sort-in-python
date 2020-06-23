def MergeShort(List):
    if len(List) > 1:
        print("Enterd in Program: "+str(List))
        Middle = len(List)//2
        Left = List[:Middle]
        print("Left: "+str(Left))
        Right = List[Middle:]
        print("Right value: "+ str(Right))
        MergeShort(Left)
        print("Pass Left: "+str(Left))
        MergeShort(Right)
        print("Pass Right: "+str(Right))
        RightIndex = 0
        LeftIndex = 0
        FinalListIndex = 0
        while RightIndex < len(Right) and LeftIndex < len(Left):
            if Left[LeftIndex] > Right[RightIndex]:
                List[FinalListIndex] = Right[RightIndex]
                RightIndex +=1
            else:
                List[FinalListIndex] = Left[LeftIndex]
                LeftIndex += 1
            FinalListIndex += 1


        while RightIndex < len(Right):
            List[FinalListIndex] = Right[RightIndex]
            RightIndex += 1
            FinalListIndex += 1

        while LeftIndex < len(Left):
            List[FinalListIndex] = Left[LeftIndex]
            LeftIndex += 1
            FinalListIndex += 1
        print("Arranged list: "+str(List[:]))

