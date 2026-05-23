# Your local library needs your help! Given the expected and actual return dates for a 
# library book, create a program that calculates the fine (if any). The fee structure 
# is as follows:
# If the book is returned on or before the expected return date, no fine will be charged 
# (i.e.:fine =0 ).
#  If the book is returned after the expected return day but still within the 
# same calendar month and year as the expected return date, fine = 15 * (number of days late).
# If the book is returned after the expected return month but still within the same 
# calendar year as the expected return date, the fine = 500 * (number of months late).
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.


# Sample Input
# 9 6 2015
# 6 6 2015
# Sample Output
# 45
# Explanation
# Given the following return dates:
# Actual:   9 June 2015
# Expected: 6 June 2015
# Because the book was returned late (but still within the same month and year), we calculate
# the fine as 15 Hackos * (number of days late). The book was 3 days late, so the fine will be
# 15 * 3 = 45 Hackos.


# Enter your code here. Read input from STDIN. Print output to STDOUT
actual_day, actual_month, actual_year = map(int, input().split())
expected_day, expected_month, expected_year = map(int, input().split())
fine = 0
if actual_year > expected_year:
    fine = 10000
elif actual_year == expected_year:
    if actual_month > expected_month:
        fine = 500 * (actual_month - expected_month)
    elif actual_month == expected_month and actual_day > expected_day:
        fine = 15 * (actual_day - expected_day)
print(fine)