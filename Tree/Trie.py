
class Trie:
    class Node:
        def __init__(self, x, bros = None, child = None):
            self.data = x
            self.bros = bros
            self.child = child

        def get_child(self, x):
            child = self.child
            while child:
                if child.data == x: break
                child = child.bros
            return child

        def set_child(self, x):
            child = Trie.Node(x, self.child)
            self.child = child
            return child


        def del_child(self, x):
            child = self.child
            if child.data == x:
                self.child = child.bros
                return True
            else:
                while child.bros:
                    if child.bros.data == x:
                        child.bros = child.bros.bros
                        return True
                    child = child.bros
            return False


        def traverse(self, leaf):
            if self.data == leaf:
                yield []
            else:
                child = self.child
                while child:
                    for x in child.traverse(leaf):
                        yield [self.data] + x
                    child = child.bros

    def __init__(self, x = None):
        self.root = Trie.Node(None)  # header
        self.leaf = x

    def search(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if not node: return False
        # check leaf
        return node.get_child(self.leaf) is not None

    def insert(self, seq):
        node = self.root
        for x in seq:
            child = node.get_child(x)
            if not child:
                child = node.set_child(x)
            node = child
        # check leaf
        if not node.get_child(self.leaf):
            node.set_child(self.leaf)

    def delete(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if not node: return False
        # delete leaf
        return node.del_child(self.leaf)

    def traverse_h(self, func):
        def traverse_node(node, buff):
            if node.data == self.leaf:
                func(buff)
            else:
                child = node.child
                while child:
                    traverse_node(child, buff + [node.data])
                    child = child.bros
        #
        node = self.root.child
        while node:
            traverse_node(node, [])
            node = node.bros

    def traverse(self):
        node = self.root.child
        while node:
            for x in node.traverse(self.leaf):
                yield x
            node = node.bros

    def common_prefix(self, seq):
        node = self.root
        buff = []
        for x in seq:
            buff.append(x)
            node = node.get_child(x)
            if not node: return
        node = node.child
        while node:
            for x in node.traverse(self.leaf):
                yield buff + x
            node = node.bros


if __name__ == '__main__':
    # suffix trie
    def make_suffix_trie(seq):
        a = Trie()
        for x in xrange(len(seq)):
            a.insert(seq[x:])
        return a

    s = make_suffix_trie('abcabbca')
    for x in s.traverse():
        print x
    for x in ['a', 'bc']:
        print x
        for y in s.common_prefix(x):
            print y