def expected_revenue(delta):
    spread = 2 * delta  
    return (1 - PI) * (PLB(spread) + PLS(spread)) * spread


def expected_profit(delta):
    return expected_revenue(delta) - expected_cost(delta)


def objective(delta):
    return -expected_profit(delta)


def find_optimal_spread():
    result = minimize(objective, x0=1, bounds=[(0.01, 5)])
    optimal_delta = result.x[0]
    optimal_bid = P0 - optimal_delta
    optimal_ask = P0 + optimal_delta

    print(f"Optimal Delta: {optimal_delta:.4f}")
    print(f"Optimal Bid: {optimal_bid:.2f}, Optimal Ask: {optimal_ask:.2f}")
    print(f"Optimal Spread: {2 * optimal_delta:.2f}")

    return optimal_bid, optimal_ask


if __name__ == "__main__":
    bid, ask = find_optimal_spread()
    print(f"Optimal Bid Price: {bid:.2f}, Optimal Ask Price: {ask:.2f}")
