from revenue import plot_expected_revenue
from optimization import find_optimal_spread
from price_simulation import plot_price_distribution, generate_price_distribution


def main():
    prices = generate_price_distribution()
    plot_price_distribution(prices)

  
    plot_expected_revenue()

    bid, ask = find_optimal_spread()
    print(f"Optimal Bid Price: {bid:.2f}, Optimal Ask Price: {ask:.2f}")


if __name__ == "__main__":
    main()
