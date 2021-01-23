class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        A=board
        for i in range(9):
            s=set()
            for j in range(9):
                if A[i][j]=='.':
                    continue
                if A[i][j] in s:
                    return False
                else:
                    s.add(A[i][j])

    #check for columns  
        for k in range(9):
            s=set()
            for l in range(9):
                if A[l][k]=='.':
                    continue
                if A[l][k] in s:
                    return False
                else:
                    s.add(A[l][k])

    #check for squares
        m=0
        while(m<9):
            n=0
            while(n<9):
                s=set()
                for i in range(n,n+3):
                    for j in range(m,m+3):
                        if A[i][j]=='.':
                            continue
                        if A[i][j] in s:
                            return False
                        else:
                            s.add(A[i][j])
                n+=3
            m+=3

        return True