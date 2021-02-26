import matplotlib.pyplot as plt


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def calculate_probability(n, d):
    return 1 - factorial(d) / ((d ** n) * factorial(d - n))


if __name__ == '__main__':
    d = [10, 50, 100, 200, 365]
    colors = ['red', 'blue', 'yellow', 'green', 'purple']

    for idx, k in enumerate(d):
        x = []
        y = []
        for i in range(k):
            x.append(i)
            y.append(calculate_probability(i, k))
        plt.plot(x, y, color=colors[idx])
    plt.show()
