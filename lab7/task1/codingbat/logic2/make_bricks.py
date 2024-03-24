
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
    # Calculate the maximum number of inches we can get from the big bricks
    max_big_inches = big * 5
    
    # If the goal is less than or equal to the maximum inches we can get from the big bricks,
    # we only need to use the big bricks to reach the goal
    if goal <= max_big_inches:
        # Check if we have enough big bricks to reach the goal
        return goal % 5 <= small
    else:
        # We need to use all the big bricks and some small bricks to reach the goal
        # Calculate the remaining inches we need to cover using the small bricks
        remaining_inches = goal - max_big_inches
        return remaining_inches <= small
