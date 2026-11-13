from collections import deque
def moving_avg_deque(r):
    w, s, out = deque(maxlen=7), 0.0, []
    for x in r:
        if len(w) == 7:
            s -= w[0]          # value that is about to fall out of the window
        w.append(x)            # deque drops the oldest value automatically
        s += x
        if len(w) == 7:
            out.append(s / 7)
    return out
 
# dictionary keyed by date (days become keys, so a late reading is just an assignment)
rain = {"2026-01-01": 2.0, "2026-01-02": 0.0}
rain["2026-01-03"] = 12.5      # O(1) average, order of arrival does not matter
