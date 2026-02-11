#check a string is it a palindrome or not!!





s = "MADAM"  

def palindrome(i, s):  
    n = len(s)  
    if(i >= n // 2):  
        return True  
    if s[i] != s[n - i - 1]: 
        return False  
    
    return palindrome(i + 1, s)  