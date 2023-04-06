
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=[]):
    """构建二叉树
    input_list: 输入数列
    """
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    print(node.data)
    return node



"""
二叉树深度优先遍历
"""
def pre_order_travelsal(node):
    """前序遍历
    根节点，左子树，右子树
    Args:
        node (_type_): 二叉树节点
    """
    if node is None:
        return None
    print(node.data)
    pre_order_travelsal(node.left)
    pre_order_travelsal(node.right)
    return node


def in_order_travelsal(node):
    """中序遍历
    左子树，根节点，右子树
    Args:
        node (_type_): 二叉树节点
    """
    if node is None:
        return None
    in_order_travelsal(node.left)
    print(node.data)
    in_order_travelsal(node.right)
    return node


def post_order_travelsal(node):
    """后序遍历
    左子树，右子树，根节点
    Args:
        node (_type_): 二叉树节点
    """
    if node is None:
        return None
    post_order_travelsal(node.left)
    post_order_travelsal(node.right)
    print(node.data)
    return node


def pre_order_travelsal_with_stack(node):
    """二叉树非递归前序遍历：栈实现

    Args:
        node (_type_): _description_
    """
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right
        


"""
二叉树广度优先遍历，依靠队列
"""
from queue import Queue

def level_order_travelsal(node):
    queue = Queue()
    queue.put(node)     # 入队
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
            


my_input_list = [3,2,9,None,None,10,None,None,8,None,4]
root = create_binary_tree(my_input_list)

# print("前序遍历：")
# pre_order_travelsal(root)

# print("栈前序遍历: ")
# pre_order_travelsal_with_stack(root)

# print("中序遍历：")
# in_order_travelsal(root)

# print("后序遍历：")
# post_order_travelsal(root)