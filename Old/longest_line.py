height = [1,8,6,2,5,4,8,3,7]
l=0
r=len(height)-1
max_area=1

while l<r:
    current_area = (r-l)*min(height[l],height[r])
    if current_area>max_area:
        max_area=current_area

    if height[l]<height[r]:
        l+=1
    else:
        r-=1    

print(max_area)