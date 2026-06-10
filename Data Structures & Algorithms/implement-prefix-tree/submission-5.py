class Node:
     def __init__(self, val=0, childs=None, final=False):
         self.val = val
         self.final = final
         self.childs = childs if childs is not None else []

class PrefixTree:

    def __init__(self):
        self.tree = Node(0)

    def insert(self, word: str) -> None: 
        current = self.tree
        for i in range(len(word)):
            c = word[i]
            child = [ elt for elt in current.childs if elt.val == c]
            node = None
            if child == []:
                node = Node(c)
                current.childs.append(node)
            else:
                node = child[0]
            if i == len(word) - 1:
                node.final = True
            current = node

    def search(self, word: str) -> bool:
        current = self.tree
        for i in range(len(word)):
            c = word[i]
            child = [ elt for elt in current.childs if elt.val == c]
            if child == []:
                return False
            current = child[0]
            if i == len(word) - 1:
                return current.final
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for i in range(len(prefix)):
            c = prefix[i]
            child = [ elt for elt in current.childs if elt.val == c]
            if child == []:
                return False
            current = child[0]
        return True