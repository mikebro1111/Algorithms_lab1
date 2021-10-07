import time
import json
import sys

from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort
from shell import shell_sort
import samplers


SAMPLERS = [("random_sampler", 5), ("random_small_sampler", 3), ("increasing_sampler", 1), ("decreasing_sampler", 1)]
SORTS = ["selection_sort", "insertion_sort", "merge_sort", "shell_sort"]


def benchmark(sort_func, array_sampler, array_size, times):
    mean_time = 0
    mean_count = 0
    for tst in range(times):
        arr = array_sampler(array_size)
        start = time.time()
        counter = sort_func(arr)
        end = time.time()
        mean_time += end - start
        mean_count += counter
    return mean_time / times, mean_count / times


if __name__ == "__main__":
    low = 7
    high = 15
    results_dict = {sampler[0]: {sort: {"time": {}, "ops": {}} for sort in SORTS} for sampler in SAMPLERS}
    for exp in range(low, high + 1):
        size = 2**exp
        for sampler, runs in SAMPLERS:
            for sort in SORTS:
                # if exp > 12 and sort in ["selection_sort", "insertion_sort" ]:
                #     continue
                wall_time, count = benchmark(getattr(sys.modules["__main__"], sort), getattr(samplers, sampler), size, runs)
                results_dict[sampler][sort]["time"][size] = wall_time
                results_dict[sampler][sort]["ops"][size] = count
    with open("test.json", "w") as f:
        json.dump(results_dict, f, indent=4)
