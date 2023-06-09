'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.


Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

'''

def compare_version(A: str, B: str) -> int:
    version1 = A.split(".")
    version2 = B.split(".")
    max_len = max(len(version1),len(version2))
    
    for i in range(max_len):
        ver1_num = 0 if (len(version1) - 1) < i else int(version1[i])
        ver2_num = 0 if (len(version2) -1) < i else int(version2[i])
        
        if ver1_num > ver2_num:
            return 1
        elif ver1_num < ver2_num:
            return -1
    
    return 0


if __name__ == "__main__":
    A = "1.0"
    B = "1"
    print(compare_version(A,B)) 