import matplotlib.pyplot as plt
import json
import math


if __name__ == "__main__":
    with open("test.json") as f:
        results = json.load(f)

    for sampler, sorts in results.items():
        f = plt.figure()
        for i, (sort, data) in enumerate(sorts.items()):
            data = data["time"]
            sizes, times = zip(*data.items())
            sizes = [int(math.log2(int(x))) for x in sizes]
            times = [math.log10(x * 1000 + 1) for x in times]
            plt.plot(sizes, times, label=sort, linewidth=1, marker= ['_', '.', 'x', 'o', '+'][i], alpha=0.5)
        plt.legend()
        plt.title(f"Time, {sampler}")
        plt.xlabel("$log_2$ size")
        plt.ylabel("Execution time, $log_{10}$ ms")
        # plt.ylabel("Execution time, s")
        plt.xticks(sizes)
        plt.savefig(f"time_{sampler}.png", dpi=150)

    for sampler, sorts in results.items():
        f = plt.figure()
        for i, (sort, data) in enumerate(sorts.items()):
            data = data["ops"]
            sizes, times = zip(*data.items())
            sizes = [int(math.log2(int(x))) for x in sizes]
            times = [math.log10(x + 1) for x in times]
            plt.plot(sizes, times, label=sort, linewidth=1, marker= ['_', '.', 'x', 'o', '+'][i], alpha=0.5)
        plt.legend()
        plt.title(f"Operations, {sampler}")
        plt.xlabel("$log_2$ size")
        # plt.ylabel("Operations, num")
        plt.ylabel("Operations, $log_{10}$ num")
        plt.xticks(sizes)
        plt.savefig(f"ops_{sampler}.png", dpi=150)