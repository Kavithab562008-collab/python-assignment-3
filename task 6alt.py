flat = [(no, station, arr, dep, days) for no, t in tt.items() for station, arr, dep in t["route"]]
def query_flat(station, day):
    return sorted([(no, dep) for no, st, arr, dep, days in flat if st == station and day in days],
                  key=lambda r: r[1])
