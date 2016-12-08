class Node:

    def __init__(self, left, right, key):
        self.left = left
        self.right = right
        self.key = key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key