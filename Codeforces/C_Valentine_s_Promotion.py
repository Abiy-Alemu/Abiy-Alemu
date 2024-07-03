# Function to calculate the maximum total value of flowers received for free for one purchase
def calculate_max_total_value(n, prices, x, y):
    prices.sort()  # Sort the prices in non-decreasing order
    total_price = sum(prices[:x])  # Calculate the sum of the first x prices
    discount_price = sum(prices[:y])  # Calculate the sum of the first y prices
    return total_price - discount_price  # Subtract the discount price from the total price

# Read the input
n, q = map(int, input().split())
prices = list(map(int, input().split()))

# Process each query
for _ in range(q):
    x, y = map(int, input().split())
    max_total_value = calculate_max_total_value(n, prices, x, y)
    print(max_total_value)
