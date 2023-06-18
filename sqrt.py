nums = [0,1,0,3,12]
last_index = 0
for i in range(len(nums)):
     if nums[i]!=0:
         nums[i],nums[last_index]=nums[last_index],nums[i]
         last_index=last_index+1
     else:
         pass
print(nums)
         
		 
		 
		 
		 
s = "aabb"

for i in range(len(s)):
     if s.count(s[i])==1:
         print(i)
         break
else:
    print(-1)
import math
x = int(input("Enter a value to find its sqrt: "))
print(math.floor(x**0.5))