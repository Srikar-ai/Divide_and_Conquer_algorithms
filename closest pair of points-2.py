#Time complexity is O(nlogn)
def Distance(p1,p2):
    a=p1[0]-p2[0]
    b=p1[1]-p2[1]
    return a**2+b**2
def Closest_Pair(l):
    m=float('inf')
    for x in range(len(l)-1):
        for y in range(x+1,len(l)):
            m=min(m,Distance(l[x], l[y]))
    return m
def Closest_pair_strip(lst,d):
    for x in range(len(lst)-1):
        for y in range(x+1,len(lst)):
            if lst[y][1]-lst[x][1]>=d:
                break
            d=min(d,Distance(lst[x], lst[y]))
    return d
def R(xpoints,ypoints):
    if len(xpoints)<=3:
        return Closest_Pair(xpoints)
    mid=len(xpoints)//2
    mid_val=xpoints[mid]
    pl=[x for x in ypoints if x[0]<=mid_val[0]]
    pr=[x for x in ypoints if x[0]> mid_val[0]]
    left=R(xpoints[:mid],pl)
    right=R(xpoints[mid:],pr)
    d=min(left,right)
    strip=[x for x in ypoints if abs(x[0]-mid_val[0])<d]                             
    return Closest_pair_strip(strip, d)
p=[[2,3],[12,30],[40,50],[5,1],[12,10],[3,3]]    
xPoints = sorted(p, key=lambda x: x[0])
yPoints = sorted(p, key=lambda x: x[1])        
print(R(xPoints,yPoints))     
