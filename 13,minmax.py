def minimax(depth, node_index, is_max, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if is_max:
        best = float('-inf')
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Example leaf node values (binary tree of depth 3, i.e. 2^3 = 8 leaf nodes)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Run the algorithm
optimal_value = minimax(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", optimal_value)

# Result
print("The program executed successfully.")
