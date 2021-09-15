def f(maxWeight, *weights):
    weight = [0] * (maxWeight + 1)
    weight[0] = 1
    for i in range(len(weights)):
        for w in range(maxWeight, weights[i] - 1, -1):
            if weight[w - weights[i]] == 1:
                weight[w] = 1

    for i in range(maxWeight, 0, -1):
        if weight[i] == 1:
            return i

maxWeight = int(input())
weights = input()
weights = weights.split(' ')
weights = [int(x) for x in weights ]

print(f(maxWeight, *weights))
