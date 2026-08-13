class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, current):
            if index == len(word):
                return current.is_end_of_word

            char = word[index]

            if char == '.':
                for child in current.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            if char not in current.children:
                return False

            return dfs(index + 1, current.children[char])

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)