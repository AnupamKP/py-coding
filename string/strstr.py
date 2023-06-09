'''
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 


Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

def strstr(haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1


if __name__ == "__main__":
    haystack = "helloworld"
    needle = "world"
    print(strstr(haystack,needle))