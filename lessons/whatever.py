def w_sum(vals):
    i = 0
    total = 0.0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total

# Part 2: f_sum function using a for loop without range
def f_sum(vals):
    total = 0.0
    for val in vals:
        total += val
    return total

# Part 3: f_range_sum function using a for loop with range
def f_range_sum(vals):
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total