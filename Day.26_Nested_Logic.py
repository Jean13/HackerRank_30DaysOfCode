# Tuple comparison
ret_d, ret_m, ret_y = [int(x) for x in input().split(' ')]
exp_d, exp_m, exp_y = [int(x) for x in input().split(' ')]

# returned on or before the expected return date; no fine
if (ret_y, ret_m, ret_d) <= (exp_y, exp_m, exp_d):
    print(0)
# returned after the expected return day but still within the same calendar month and year as the expected return date
elif (ret_y, ret_m) == (exp_y, exp_m):
    print(15 * (ret_d - exp_d))
# returned after the expected return month but still within the same calendar year as the expected return date
elif ret_y == exp_y:
    print(500 * (ret_m - exp_m))
# returned after the calendar year in which it was expected
else:
    print(10000)

