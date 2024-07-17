def knapsack(items, maxWeight):
    n = len(items)
    V = [[0] * (maxWeight + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(maxWeight + 1):
            if items[i-1][1] <= w:
                V[i][w] = max(V[i-1][w], V[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                V[i][w] = V[i-1][w]
    w = maxWeight
    selected = []
    for i in range(n, 0, -1):
        if V[i][w] != V[i-1][w]:
            selected.append(items[i-1])
            w -= items[i-1][1]
    selected.reverse()
    return V[n][maxWeight], selected

# User input for items and maximum weight
num_items = int(input("Enter the number of items: "))
items = []
for i in range(num_items):
    item_id = i + 1
    weight = int(input(f"Enter weight for item {item_id}: "))
    value = int(input(f"Enter value for item {item_id}: "))
    items.append((item_id, weight, value))

maxWeight = int(input("Enter the maximum weight capacity of the knapsack: "))

maxValue, selected = knapsack(items, maxWeight)

print("Maximum Value:", maxValue)
print("Selected Items:", selected)
