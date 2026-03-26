# def recursionPermute(index,s,ans):
#     if index==len(s):
#         ans.append("".join(s))
#         return ans
#     for i in range(index,len(s)):
#         s[index],s[i]=s[i],s[index]
#         recursionPermute(index+1,s,ans)
#         s[index],s[i]=s[i],s[index]

# def findPermutation(s):
#     ans=[]
#     recursionPermute(0,list(s),ans)
#     ans.sort()
#     return ans
# if __name__=="__main__":
#     s='ABC'
#     res=findPermutation(s)
#     for n in res:
#         print(n)

# find the permutation of unique value
# def genPermutation(index, s, used, curr, st):
#     if index == len(s):
#         st.add(''.join(curr))
#         return

#     for j in range(len(s)):
#         if not used[j]:
#             used[j] = True
#             curr.append(s[j])

#             genPermutation(index + 1, s, used, curr, st)

#             used[j] = False
#             curr.pop()


# def findPermutation(s):
#     used = [False] * len(s)
#     st = set()
#     curr = []
#     genPermutation(0, s, used, curr, st)
#     return list(st)


# if __name__ == "__main__":
#     s = 'BB'
#     print(findPermutation(s))

# def subsets(nums):
#     result=[]
#     path=[]
#     def backtrack(index):
#         if index==len(nums):
#             result.append(path[:])
#             return
#         path.append(nums[index])
#         backtrack(index+1)
#         path.pop()
#         backtrack(index+1)
#     backtrack(0)
#     return result
# nums=[1,2]
# listdemo=subsets(nums)
# print(subsets(nums))
# print(len(listdemo))

def subsets(nums):
    result=[]
    path=[]
    def backtrack(start):
        result.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return result


# def subsetswithDup(nums):
#     nums.sort()
#     result=[]
#     path=[]
#     def backtrack(index)

# def findPath(maze,n):
#     result=[]
#     if maze[0][0]==0:
#         return result
#     visited=[[False for _ in range(n)] for _ in range(n)]
#     directions='DLRU'
#     dr=[1,0,0,-1]
#     dc=[0,-1,1,0]
#     def backtrack(r,c,path):
#         #reached desintaion
#         if r==n-1 and c==n-1:
#             result.append(path)
#             return
#         visited[r][c]=True
#         for i in range(4):
#             nr=r+dr[i]
#             nc=c+dc[i]
#             if 0<=nr<n and 0<=nc<n and maze[nr][nc]==1 and not visited[nr][nc]:
#                 backtrack(nr,nc,path+directions[i])
#         visited[r][c]=False
#     backtrack(0,0,"")
#     return result

# def solveNQueens(n):
#     result=[]
#     board=[['.' for _  in range(n)] for _ in range(n)]
#     cols=set()
#     diag1=set()
#     diag2=set()
#     def backtrack(row):
#         if row == n:
#             temp=[''.join(r) for r in board]
#             result.append(temp)
#             return
#         for col in range(n):
#             if col in cols or (row-col) in diag1 or (row+col) in diag2:
#                 continue

def solveNqueen(n):
    result=[]
    board=[['.' for _ in range(n)] for _ in range(n)]
    cols=set()
    diag1=set()
    diag2=set()
    def backtrack(row):
        if row==n:
            temp=[''.join(r) for r in board]
            result.append(temp)
            return
        for col in range(n):
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue
            board[row][col]='Q'
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            backtrack(row+1)
            board[row][col]='.'
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)
    backtrack(0)
    return result
answers = solveNqueen(4)

for solution in answers:
    for row in solution:
        print(row)
    print()

def solveSudoku(board):
    def is_valid(row, col, num):
        # check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if is_valid(row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            board[row][col] = "."   # backtrack

                    return False   # no number fits here

        return True   # solved

    backtrack()