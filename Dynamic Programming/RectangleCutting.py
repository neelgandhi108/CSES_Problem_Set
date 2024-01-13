# Rectangle Cutting

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = float('inf')
        self.dfs(0,0,[[False]*m for _ in range(n)],0)
        return self.ans - 1
    
    # (r,c) -> starting point for selecting a square
    # rect -> record status of curr rectangle
    # cnt - > num of squares we have covered
    def dfs(self,r,c,rect,cnt):
        n , m = len(rect) , len(rect[0])
        # Optimization : curr cnt >= curr ans
        if cnt >= self.ans:
            return
        # Successfully cover whole rectangle
        if r >= n:
            self.ans = cnt
            return
        # Successfully cover area [0,..,n][0,..,c] -> Move to next row
        if c >= m:
            self.dfs(r+1,0,rect,cnt)
            return
        # if (r,c) is already covered -> move to next point(r,c+1)
        if rect[r][c]:
            self.dfs(r,c+1,rect,cnt)
            return
        # Try all possible size of squares starting from (r,c)
        for k in range(min(n-r,m-c),0,-1):
            if self.isAvailable(rect,r,c,k):
                # Backtracking
                self.cover(rect,r,c,k)
                self.dfs(r,c+1,rect,cnt+1)
                self.uncover(rect,r,c,k)
    
    # Check if area is already covered
    def isAvailable(self,rect,r,c,k):
        for i in range(k):
            for j in range(k):
                if rect[r+i][c+j]:
                    return False
        return True
    
    # Cover the area with k*k square
    def cover(self,rect,r,c,k):
        for i in range(k):
            for j in range(k):
                rect[r+i][c+j] = True

    # Uncover the area
    def uncover(self,rect,r,c,k):
        for i in range(k):
            for j in range(k):
                rect[r+i][c+j] = False

# Accepting input from the user
A, B = map(int, input().split())

# Finding the minimum number of cuts
sol = Solution()
result = sol.tilingRectangle(A, B)
print(result)

