N = int(input())

cost = list(map(int, input().split()))
type_ = list(map(int, input().split()))
translators = [cost[i] for i in range(N) if type_[i] == 1]+[float('inf')]
authors = [cost[i] for i in range(N) if type_[i] == 2]+[float('inf')]
author_translators = [cost[i] for i in range(N) if type_[i] == 3]+[float('inf')]

minimum_coin = min(min(translators)+min(authors), min(author_translators))
print(minimum_coin)
