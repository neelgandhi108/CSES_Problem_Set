# Initialize variables
n = int(input())
s = 0
p = []
hull = []

# Read n points to p list 
for i in range(n):
    x, y = map(int, input().split()) 
    p.append([x, y])
    
# Sort points
p.sort()

for t in range(2):

    for i in range(n):
       
        # Pop points from hull until cross product condition is satisfied
        while len(hull) - s >= 2:
            p1 = hull[-2]
            p2 = hull[-1]
            if (p2[0] - p1[0]) * (p[-1][1] - p1[1]) - (p2[1] - p1[1]) * (p[-1][0] - p1[0]) <= 0:
                break
            hull.pop()
            
        hull.append(p[i])
        
    # Remove last point  
    hull.pop() 
    s = len(hull)
    
    # Reverse points
    p.reverse()
    
print(s)
for h in hull:
    print(h[0], h[1])