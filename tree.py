class Tree:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def __iadd__(self, child):
        child.parent = self
        self.children.append(child)
        return self

    def fromString(string):
        return Tree.fromList(string.split())

    def fromList(list):
        itemList = list[0].lstrip('()')
        itemList = itemList.rstrip('()')
        node = Tree (itemList)
        list = list[1:]

        while len(list) > 0 and "(" in list[0]:
            child, list = Tree.fromList(list)
            child.value = child.value.lstrip('()')
            node += child

        endlist = list
        itemAddedCount = 0

        while len(endlist) > 0 and "(" not in endlist[0]:
            node += Tree(endlist[0].rstrip('()'))
            itemAddedCount += 1

            if ")" in endlist[0]:
                return node, list[itemAddedCount:]
            endlist = endlist[1:]

        return node, list[1:]

    def show(self,lvl=0):
        lvl +=1

        if lvl == 1:
            print(self.value + " " + str(lvl))
        elif lvl == 2:
            print("+",end='')
            print("--", end='')
            print(" " + self.value + " " + str(lvl))
        else:
            print("|", end='')

            for i in range(1, lvl-2):
                print(" ", end='')

            for i in range(1, (lvl-2)*3+1):
                print(" ", end='')

            print("+--", end='')

            if self.parent != None:
                print(" ",end='')
            print(self.value + " " + str(lvl))

        for item in self.children:
            item.show(lvl)

    def __repr__(self):
        return '{}{}'.format(self.value, ': {}'.format(self.children) if self.children else '')


if __name__ == "__main__":

    text = "(asciitree (sometimes you) (just (want to draw)) trees (in (your terminal)))"
    example_tree, list = Tree.fromString(text)
    print(example_tree)
    example_tree.show()

