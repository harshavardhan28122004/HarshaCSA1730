class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def alpha_beta(node, depth, maximizing_player, alpha, beta):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example tree from your notebook
if __name__ == "__main__":
    root = Node(0)

    child1 = Node(3)
    child2 = Node(5)
    child3 = Node(6)
    child4 = Node(9)
    child5 = Node(2)
    child6 = Node(1)

    root.children = [child1, child2, child3]
    child1.children = [child4, child5]
    child2.children = [child6]

    depth = 3
    result = alpha_beta(root, depth, True, float('-inf'), float('inf'))

    print("Optimal value is:", result)
    print("The program executed successfully.")
