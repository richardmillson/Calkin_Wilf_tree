from tree import *
import matplotlib.pyplot as plt


def plot_distribution(n):
    """
    plot the distribution of the first n elements over the reals
    :param n: positive int
    :return: matplotlib plot side effect
    """
    x = get_slice(0, n)
    y = [position for position in range(1, len(x) + 1)]
    plt.plot(x, y, "o")
    plt.axis([0, int(math.floor(math.log(n, 2))) + 1, -1, n + 1])
    plt.show()
