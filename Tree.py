class TreeNode:
    def __init__(self, value: any | None,feature :str, firstChild : int = -1, nextSubnit: int = -1, parent: int = 0):
        self.feature = feature
        self.value = value
        self.firstChild = firstChild
        self.nextSubnit = nextSubnit
        self.parent = parent


class FlattenedArray:
    def __init__(self, root: TreeNode = TreeNode(None)):
        self.root = root
        self.data = [self.root.value]
        self.firstChilds = [-1]
        self.nextSubnit = [-1]
        self.size = 1

    def add(self, node: TreeNode):
        self.data.append(node.value)
        self.firstChilds.append(node.firstChild)
        self.nextSubnit.append(node.nextSubnit)
        index = self.size
        self.size += 1
    

        if self.firstChilds[node.parent] == -1:
            self.firstChilds[node.parent] = index
        else:
            current = self.firstChilds[node.parent]
            while  self.nextSubnit[current] != -1 :
                current = self.nextSubnit[current]

            self.nextSubnit[current] = index

    def delete(self, index):
        
        self.data[index] = None



