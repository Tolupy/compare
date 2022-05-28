# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    
    # the sorted strings are checked
    if(sorted(str1)== sorted(str2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="race"
s2 ="care"
find_anagram(s1, s2)
    # return True

