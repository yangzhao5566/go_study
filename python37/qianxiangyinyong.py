from __future__ import annotations


class Tree:
    def __init__(self, left: Tree, right: Tree) -> None:
        self.left = left
        self.right = right

    """
    通过__future__ 模块的annotation 这样可以避免前向引用的问题,
    def __init__(self, left: "Tree", right: "Tree") -> None:
        self.left = left
        self.right = right
    """