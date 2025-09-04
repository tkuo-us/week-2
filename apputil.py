import numpy as np


# update/add code below ...

def ways(n: int) -> int:
    """
    Return the number of ways to make n cents using only pennies (1) and nickels (5).
    With k nickels (k = 0..n//5), the remaining cents are filled by pennies uniquely.
    Therefore, the count is floor(n/5) + 1. For n < 0, return 0.
    """
    if n < 0:
        return 0
    return n // 5 + 1

def lowest_score(names: np.ndarray, scores: np.ndarray) -> str:
    """
    Return the name of the student with the lowest score.
    `names` and `scores` should be 1-D NumPy arrays of equal length.
    """
    idx = np.argmin(scores)
    return str(names[idx])

def sort_names(names: np.ndarray, scores: np.ndarray):
    """
    Return a list of (name, score) pairs sorted by score in descending order.
    """
    order = np.argsort(scores)[::-1]
    return [(str(names[i]), int(scores[i])) for i in order]


def waysoptional(cents, coin_types=[1, 5]):
    """
    Return the number of waysoptional to make `cents` using coins in coin_types.
    Order of coins does not matter (combinations, not permutations).
    """
    dp = [0] * (cents + 1)
    dp[0] = 1  

    for coin in coin_types:
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]

    return dp[cents]