class TrieNode:
    def __init__(self):
        self.nxt = {}
        self.isLast = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        i = 0

        while i < len(word):
            if word[i] not in cur.nxt:
                cur.nxt[word[i]] = TrieNode()
            cur = cur.nxt[word[i]]

            i += 1

        cur.isLast = True

    def search(self, word: str) -> bool:
        def recurse(i, cur):

            while i < len(word):
                if word[i] == ".":
                    any_match = False
                    for c in cur.nxt:
                        any_match |= recurse(i + 1, cur.nxt[c])
                    return any_match
                elif word[i] not in cur.nxt:
                    return False
                else:
                    cur = cur.nxt[word[i]]
                
                i += 1
            
            return cur.isLast

        return recurse(0, self.root)
