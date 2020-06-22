def MergeShort(List):
    if len(List) > 1:
        Middle = len(List)//2
        Right = List[Middle:]
        Left = List[:Middle]
        MergeShort(Left)
        MergeShort(Right)
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
