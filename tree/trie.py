class Trie:
    class Node: 
        def __init__(self): 
            self.child_node = [None]*26
            self.is_end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node() 
        
    def char_to_index(self,ch): 
        return ord(ch) - ord('a')
    
    def insert_word(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root 
        for char in word: 
            index = self.char_to_index(char) 
            if not curr.child_node[index]: 
                curr.child_node[index] = self.Node()
            curr = curr.child_node[index]  
        curr.is_end = True
        
    def search_word(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root 
        if '.' not in word:
            for char in word: 
                index = self.char_to_index(char) 
                if not curr.child_node[index]: 
                    return False
                curr = curr.child_node[index] 
        else:
            return False
        return curr != None and curr.is_end 


if __name__ == "__main__":
    trie = Trie()
    trie.insert_word('anupam')
    trie.insert_word('pathi')
    print(trie.search_word('pathi'))