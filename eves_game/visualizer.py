import matplotlib.pyplot as plt


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def calculate_collision_probability(n, d):
    """
    :param n: Current count
    :param d: Hash table size
    :return: Probability of collision
    """
    return 1 - factorial(d) / ((d ** n) * factorial(d - n))


def visualize():
    d = [10, 50, 100, 200, 365]
    colors = ['red', 'blue', 'yellow', 'green', 'purple']
    for idx, k in enumerate(d):
        x = []
        y = []
        for i in range(k):
            x.append(i)
            y.append(calculate_collision_probability(i, k))
        plt.plot(x, y, color=colors[idx])
    plt.show()


if __name__ == '__main__':
    visualize()
