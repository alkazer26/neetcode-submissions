class TrieNode:
    def __init__(self, val="", isLast=False, nxt=None):
        self.val = val

        if nxt is None:
            nxt = {}
        self.nxt = nxt  # {"char" : "TrieNode"}

        self.isLast = isLast


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        i = 0
        cur = self.root

        while i < len(word):
            if word[i] in cur.nxt:
                cur = cur.nxt[word[i]]
            else:
                last_flag = i == len(word) - 1
                cur.nxt[word[i]] = TrieNode(word[i], last_flag)
                cur = cur.nxt[word[i]]

            i += 1

        cur.isLast = True

    def search(self, word: str) -> bool:
        i = 0
        cur = self.root

        while i < len(word):
            if word[i] not in cur.nxt:
                return False
            else:
                cur = cur.nxt[word[i]]

            i += 1

        return cur.isLast

    def startsWith(self, prefix: str) -> bool:
        i = 0
        cur = self.root

        while i < len(prefix):
            if prefix[i] not in cur.nxt:
                return False
            else:
                cur = cur.nxt[prefix[i]]

            i += 1

        return prefix[i - 1] == cur.val
