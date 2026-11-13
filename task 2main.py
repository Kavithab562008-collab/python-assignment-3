import copy, sys, time
# ---- Complete the Code ----
rows, cols = 3, 4
bad = [[0] * cols] * rows            # every row is the SAME list object
bad[0][1] = 7
good = [[0 for _ in range(cols)] for _ in range(rows)]   # TODO 1 solved
good[0][1] = 7
print("bad:", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])
stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
print(stops[(13.0418, 80.2341)])
print("\n--- list as dictionary key ---")
try:
    stops[[13.0418, 80.2341]] = "T. Nagar"
except TypeError as e:
    print("TypeError:", e)
print("\n--- id() proof ---")
print("ids of bad rows :", [id(r) for r in bad])
print("ids of good rows:", [id(r) for r in good])
print("\n--- aliasing, shallow copy, deep copy ---")
orig = [[1, 2], [3, 4]]
alias = orig
shallow1 = copy.copy(orig)
shallow2 = orig[:]
deep = copy.deepcopy(orig)
orig[0][0] = 99      # change an inner list
orig.append([5, 6])  # change the outer list
print("orig    :", orig)
print("alias   :", alias, "(same object:", alias is orig, ")")
print("copy.copy:", shallow1, "| slice copy:", shallow2)
print("deepcopy:", deep)
print("\n--- tuple unpacking in a for loop ---")
route = [("Chennai Central", 13.0827, 80.2707), ("T. Nagar", 13.0418, 80.2341)]
for name, lat, lon in route:
    print(f"{name:16s} lat={lat} lon={lon}")
print("\n--- function mutating its argument ---")
def add_stop(lst):
    lst.append("Guindy")
def add_stop_safe(lst):
    lst = lst + ["Guindy"]
    return lst
a = ["Adyar"]; add_stop(a); print("after add_stop      :", a)
b = ["Adyar"]; add_stop_safe(b); print("after add_stop_safe :", b)
print("\n--- memory: list vs tuple of 1,000,000 values ---")
L = list(range(1_000_000)); T = tuple(L)
print("list :", sys.getsizeof(L), "bytes")
print("tuple:", sys.getsizeof(T), "bytes")
print("\n--- time: create and index (1,000,000 values, best of 5) ---")
def best(f, k=5):
    m = 1e9
    for _ in range(k):
        t = time.perf_counter(); f(); m = min(m, time.perf_counter() - t)
    return m
print(f"create list : {best(lambda: list(range(1_000_000))):.5f} s")
print(f"create tuple: {best(lambda: tuple(range(1_000_000))):.5f} s")
def idx(c):
    s = 0
    for i in range(0, 1_000_000, 10):
        s += c[i]
    return s
print(f"index list  : {best(lambda: idx(L)):.5f} s")
print(f"index tuple : {best(lambda: idx(T)):.5f} s")
print("\n--- list inside a tuple ---")
t = (1, [10, 20], 3)
try:
    t[1] = [0]
except TypeError as e:
    print("t[1] = [0] ->", "TypeError:", e)
t[1].append(30)
print("t[1].append(30) works ->", t)
try:
    t[1] += [40]
except TypeError as e:
    print("t[1] += [40] -> TypeError:", e)
print("but the list still changed ->", t)
print("\n--- alternative: dictionary grid (sparse) ---")
grid = {}
for zone in [(0, 1), (0, 1), (2, 3)]:
    grid[zone] = grid.get(zone, 0) + 1
print(grid, "| zone (1,1) ->", grid.get((1, 1), 0))
big_rows = big_cols = 1000
full = [[0 for _ in range(big_cols)] for _ in range(big_rows)]
sp = {(5, 5): 1, (10, 20): 3}
print("1000x1000 list-of-lists outer+rows bytes:", sys.getsizeof(full) + sum(sys.getsizeof(r) for r in full))
print("sparse dict with 2 zones bytes:", sys.getsizeof(sp))
