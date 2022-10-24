class TreeObj:
    def __init__(self, indx: int, value: str = None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj = None, left: bool = True):
        if node:
            if left is True:
                node.left = obj
            elif left is False:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root: TreeObj, x: list):
        curr = root
        while curr.value is None:
            if x[curr.indx]:
                curr = curr.left
            else:
                curr = curr.right
        return curr.value


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)

