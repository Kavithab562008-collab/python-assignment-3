total = sum(c for c in readings if -50 <= c <= 50)      # no list is built
count = sum(1 for c in readings if -50 <= c <= 50)
# the list version  sum([c for c in readings if -50 <= c <= 50])  builds n values first
