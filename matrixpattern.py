def spirallyTraverse(mat):
    m = len(mat)
    n = len(mat[0])

    res = []
    vis = [[False] * n for _ in range(m)]

    # Change in row index for each direction
    dr = [0, 1, 0, -1]

    # Change in column index for each direction
    dc = [1, 0, -1, 0]

    # Initial position in the matrix
    r, c = 0, 0

    # Initial direction index (0 corresponds to 'right')
    idx = 0

    for _ in range(m * n):
        res.append(mat[r][c])
        vis[r][c] = True

        # Calculate the next cell coordinates based on
        # current direction
        newR, newC = r + dr[idx], c + dc[idx]

        # Check if the next cell is within bounds and not
        # visited
        if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:

            # Move to the next row
            r, c = newR, newC
        else:

            # Change direction (turn clockwise)
            idx = (idx + 1) % 4

            # Move to the next row according to new
            # direction
            r += dr[idx]

            # Move to the next column according to new
            # direction
            c += dc[idx]

    return res

# method 2
# [Expected Approach] Using Boundary Traversal - O(m*n) Time and O(1) Space
def spirallyTraverse(mat):
    m,n=len(mat),len(mat[0])
    res=[]
    top,bottom,left,right=0,m-1,0,n-1
    while top <= bottom and left <= right:
        for i in range(left,right+1):
            res.append(mat[top][i])
        top+=1

        for i in range(top,bottom+1):
            res.append(mat[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                res.append(mat[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                res.append(mat[i][left])
            left+=1
    return res