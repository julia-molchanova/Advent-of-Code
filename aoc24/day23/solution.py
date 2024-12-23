import time
from functools import cache
from collections import defaultdict


def parse_data(lines: list[str]):
    adj = defaultdict(set)
    for line in lines:
        c1, c2 = line.split("-")
        adj[c1].add(c2)
        adj[c2].add(c1)
        adj[c1].add(c1)
        adj[c2].add(c2)
    return adj, None


def print_time(user_function):
    def decorator(*args, **kwargs):
        start = time.time()
        res = user_function(*args, **kwargs)
        print(time.time() - start)
        return res

    return decorator


@print_time
def solve_part1(adj: defaultdict[set], dummy: None) -> int:
    sets = set()

    for key in adj:
        if key[0] != "t":
            continue
        for v1 in adj[key]:
            for v2 in adj[key]:
                if v2 == v1 or v2 not in adj[v1]:
                    continue
                group = sorted([v1, v2, key])
                sets.add(tuple(group))

    print([len(adj[x]) for x in adj], len(adj))

    return len(sets)


@print_time
def solve_part2(adj: defaultdict[set], dummy: None):
    # don't ever do that, highly dependent on data
    # though you can probably fit one more extra vertex for it to stay computable

    best_length = 0
    best_set = None

    for key in adj:
        for extra in adj[key]:
            neighbors = adj[key] - {extra}
            valid = True
            for v in neighbors:
                if len(neighbors - adj[v]) > 0:
                    valid = False

            if valid:
                best_set = {key} | neighbors

    print(",".join(sorted(list(best_set))))

    return best_length
