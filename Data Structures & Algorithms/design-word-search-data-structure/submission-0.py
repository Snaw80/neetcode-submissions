class Node:
     def __init__(self, val=0, childs=None, final=False):
         self.val = val
         self.final = final
         self.childs = childs if childs is not None else []

class WordDictionary:

    def __init__(self):
        self.tree = Node(0)

    def addWord(self, word: str) -> None: 
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
        currents = [self.tree]
        for i in range(len(word)):
            c = word[i]
            next_currents = []
            for current in currents:
                child = [ elt for elt in current.childs if (c == '.' or elt.val == c)]
                if child == []:
                    continue

                next_currents += child
            
            currents = next_currents
            if not currents:
                return False

        return any(node.final for node in currents)