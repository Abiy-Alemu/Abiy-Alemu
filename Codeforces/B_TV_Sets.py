
n, m = map(int, input().split())
prices = list(map(int, input().split()))
negative_prices = [price for price in prices if price < 0]
negative_prices.sort()
max_earn = sum(negative_prices[:m])
print(-max_earn)
