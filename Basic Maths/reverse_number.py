def digit_extraction(nums):
    ans = 0
    rem=0
    while nums>0:
        rem=(nums%10)
        nums=nums//10
        ans =ans*10+rem
        
    return ans
    
    
    
    
    
    
print(digit_extraction(7789))