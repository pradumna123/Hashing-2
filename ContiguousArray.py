# lc 525. Contiguous Array


# maintain a sum
# add sum to a hashmap along with the index
# if we find a sum that is already in hashmap --> get the index (cur_idx-index)
# if the val is more than global maximum change global else 
# goahead


# O(n) -- time and O(n) space

# if we encounter a sum
def findMaxLength(nums):
    if len(nums)<=1:
        return 0
    
    cu={}
    
    
    count=0
    
    
    max_val=0
    
    cu[0]=-1
    idx_c=0
    for i in nums:
        val=1 if i==1 else -1
        
        count+=val
        
        if count in cu:
            idx=cu[count]
            max_val=max(idx_c-idx, max_val)
        else:
            cu[count]=idx_c
        
        idx_c+=1
        
    
    return max_val