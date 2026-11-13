import random, time, string
from collections import Counter
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}
def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts
def top(counts, k):
    return sorted(counts.items(), key=lambda p: (-p[1], p[0]))[:k]
print(top(frequencies(calls, STOP), 3))
# ---- extra: setdefault, grouping, cleaning ----
def frequencies_setdefault(texts, stop):
    counts = {}
    for text in texts:
        for w in text.split():
            if w not in stop:
                counts.setdefault(w, 0)
                counts[w] += 1
    return counts
print("setdefault version same:", frequencies_setdefault(calls, STOP) == frequencies(calls, STOP))
complaints = [("Thanjavur", "paddy pest attack"), ("Madurai", "seeds not received"),
              ("Thanjavur", "fertiliser price high"), ("Salem", "seeds delayed"), ("Madurai", "pump subsidy"), ("Salem", "cotton leaf curl")]
by_district = {}
for district, text in complaints:
    by_district.setdefault(district, []).append(text)
print("by district:", by_district)
print("count per district:", {d: len(v) for d, v in by_district.items()})
CROPS = {"paddy", "wheat", "cotton"}
by_crop = {}
for district, text in complaints:
    for w in text.split():
        if w in CROPS:
            by_crop.setdefault(w, []).append(text)
print("by crop:", by_crop)
def clean(text):
    return "".join(ch for ch in text.lower() if ch not in string.punctuation)
print("\n--- tests: empty, case, punctuation ---")
print("empty text   :", frequencies([""], STOP), top(frequencies([""], STOP), 3))
print("no texts     :", frequencies([], STOP))
raw = ["Seeds, SEEDS! seeds.", "Price HIGH?"]
print("raw (no clean):", frequencies(raw, STOP))
print("with clean    :", frequencies([clean(t) for t in raw], STOP))
print("\n--- views ---")
d = {"seeds": 3, "price": 2}
print(d.keys(), d.values(), d.items())
d["rain"] = 1
print("views are live ->", list(d.keys()))
# ---- timing ----
random.seed(1)
vocab = ["seeds", "fertiliser", "price", "high", "delayed", "received", "subsidy", "pump", "water", "loan",
         "insurance", "pest", "paddy", "wheat", "cotton", "market", "credit", "rain", "drought", "tractor"] + \
        [f"word{i}" for i in range(180)]
def make(n):
    return [" ".join(random.choice(vocab) for _ in range(8)) for _ in range(n)]
def count_listcount(texts, stop):
    words = [w for t in texts for w in t.split() if w not in stop]
    return {w: words.count(w) for w in set(words)}
def count_counter(texts, stop):
    return Counter(w for t in texts for w in t.split() if w not in stop)
def best(f, k=3):
    m = 1e9
    for _ in range(k):
        t = time.perf_counter(); f(); m = min(m, time.perf_counter() - t)
    return m
print("\n--- timing (seconds), 8 words per complaint, 200-word vocabulary ---")
print(f"{'complaints':>10} {'dict.get':>10} {'list.count':>11} {'Counter':>10}")
for n in (1000, 10000, 100000):
    texts = make(n)
    t1 = best(lambda: frequencies(texts, STOP))
    if n <= 10000:
        t2 = best(lambda: count_listcount(texts, STOP), 1)
    else:
        t2 = best(lambda: count_listcount(texts, STOP), 1)
    t3 = best(lambda: count_counter(texts, STOP))
    same = frequencies(texts, STOP) == dict(count_counter(texts, STOP)) == count_listcount(texts, STOP)
    print(f"{n:>10} {t1:>10.4f} {t2:>11.4f} {t3:>10.4f}   identical={same}")
