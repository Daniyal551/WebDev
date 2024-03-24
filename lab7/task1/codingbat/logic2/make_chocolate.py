
# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2
def make_chocolate(small, big, goal):
    # Compute the maximum number of big bars we can use
    max_big_bars = goal // 5
    if big >= max_big_bars:
        # We have enough big bars, so we can use all of them
        goal -= max_big_bars * 5
    else:
        # We don't have enough big bars, so we use all of them and subtract their weight from the goal
        goal -= big * 5
    
    # Check if we can use enough small bars to reach the goal
    if small >= goal:
        return goal
    else:
        return -1
