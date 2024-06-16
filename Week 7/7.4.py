Coders here is a simple task for you, Given string str. Your task is to check whether it is a binary string or not by using python set.

Examples:  

Input: str = "01010101010"

Output: Yes



Input: str = "REC101"

Output: No


For example:

Input	Result
01010101010
Yes
010101 10101
No
def is_binary_string(s):
    return set(s) <= {'0', '1'}

str1 = input()


print("Yes" if is_binary_string(str1) else "No")
Input	Expected	Got	
01010101010
Yes
Yes
REC123
No
No
010101 10101
No
No
