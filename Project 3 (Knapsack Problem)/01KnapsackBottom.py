def BottomUpKnapSack(c,n,p,w):
    P = [0 for i in range (c+1)]

    for i in range(1,c+1):
        for j in range(n):
            if w[j] <= i: 
                P[i] = max(P[i], P[i-w[j]] + p[j]) #Updates each P[i] with the max profit
    print({i:P[i] for i in range(c+1)})
    return P[c]


#Part A
Capacity = 14
n = 3
weight = [4,6,8]
value = [7,6,9]

print("Part A")
print("--------------------")
print("Capacity is", Capacity)
print("Number of items is", n)
print("Weights are", weight)
print("Profit Values are", value)

print("Maximum Profit is ", BottomUpKnapSack(Capacity,n,value,weight))

#Part B
weight = [5,6,8]
value = [7,6,9]

print("\nPart B")
print("--------------------")
print("Capacity is", Capacity)
print("Number of items is", n)
print("Weights are", weight)
print("Values are", value)
print("Maximum Profit is", BottomUpKnapSack(Capacity,n,value,weight))