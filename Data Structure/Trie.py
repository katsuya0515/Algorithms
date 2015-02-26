
class Trie:
    class Node:
        def __init__(self, x, bros = None, child = None):
            self.data = x
            self.bros = bros
            self.child = child