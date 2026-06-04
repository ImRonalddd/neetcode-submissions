class Node:
    def __init__(self):
        self.children: dict[str, "Node"]={}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()

    def _walk(self, path: str) -> Node:
        node = self.root
        if path != "/":
            for part in path.split("/")[1:]:
                node = node.children.setdefault(part,Node())
        return node

    def ls(self, path: str) -> List[str]:
        node = self._walk(path)
        if node.content:
            return [path.split("/")[-1]]
        return sorted(node.children)

    def mkdir(self, path: str) -> None:
        self._walk(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self._walk(filePath).content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self._walk(filePath).content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
