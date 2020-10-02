'''
Given an array of strings, list the group anagrams together (strings with same alphabets but in same/different order).

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
["ate","eat","tea"],
["nat","tan"],
["bat"]
]
'''

from collections import defaultdict

def get_anagrams_matrices(input: list) -> list:
    anagrams_matrix = defaultdict(list)
    '''
    Learning: tuple/str can be a key but a list cannot for a dict
    '''
    for item in input:
        key = tuple(sorted(item))
        anagrams_matrix[key].append(item) 

    return list(anagrams_matrix.values())

if __name__ == "__main__":
    A = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(get_anagrams_matrices(A))