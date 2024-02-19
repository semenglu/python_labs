#Выборы в США

results = {}
n = int(input())

for i in range(n):
    record = input().split()
    for i in range(1, len(record)):
        candidate, votes = record[i-1], int(record[i])
        if candidate in results:
            results[candidate] += votes
        else:
            results[candidate] = votes

for candidate in sorted(results.keys()):
    print(candidate, results[candidate])
