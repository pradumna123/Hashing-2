# Lc-409

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


# here we count number of elements
# add all even
# add all even part of odd
# add only one odd in middle .

# O(n) time and space complexity

i1 = "abccccdd"

i2="aa"

def Solution(s):

    counts={}

    for c in s :
        counts[c]=counts.get(c,0)+1
    result, odd_found=0,False
    for _ , c in counts.items():
        if c%2==0: result+=c
        else:
            odd_found=True
            result+=c-1

        
    if odd_found: result+=1

    return result



val2=Solution(i2)
val1=Solution(i1)

print(' for {} longest palindrome of length is {} '.format(i1,val1))


print(' for {} longest palindrome of length is {} '.format(i2,val2))