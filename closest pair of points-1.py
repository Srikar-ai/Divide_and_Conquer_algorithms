#time complexity is O(n(logn)^2) not O(nlogn)
def Distance(point1,point2):
    a=point1[0]-point2[0]
    b=point1[1]-point2[1]
    return a**2+b**2
def Find_Pair(points,points_count, minv=float('inf')):

    for x in range(points_count-1):
        for y in range(x+1,points_count):
            if Distance(points[x], points[y])<minv:
                minv=Distance(points[x], points[y])
    return minv
def Find_Pair_Strip(points,points_count,minv=float('inf')):

    for x in range(points_count-1):
        for y in range(x+1,points_count):
            if points[y][1]-points[x][1]<minv:  
                minv=Distance(points[x], points[y])
    return minv
def Recursive(points_x,points_y,points_count):
    if points_count<=3:return Find_Pair(points_x,len(points_x))
    mid=points_count//2
    midpoint=points_x[mid]
    LEFT=Recursive(points_x[:mid],points_y,mid)
    RIGHT=Recursive(points_x[mid:],points_y, points_count-mid)
    minipair=min(LEFT,RIGHT)
    strip=[]
    for x  in  points_x:
        if abs(x[0]-points_x[mid][0])<minipair:
            strip.append(x)
    stripmin=Find_Pair(strip, len(strip),minipair)
    miniof=min(stripmin,minipair)
    return miniof
def C(points):
    points_x=sorted(points,key=lambda x:x[0])
    points_y=sorted(points,key=lambda x:x[1])
    points_count=len(points_x)
    return (Recursive(points_x, points_y, points_count)   )
points=[[-980,-403],[-578,910],[-568,-591],[47,244],[78,-198],[140,-800],[314,165],[646,-808],[889,-741],[980,-733]]
print(C(points)) 
