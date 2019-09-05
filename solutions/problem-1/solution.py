"""
Basically, we're getting all multiples from 3 and 5, and
reducing the multiples from 15 (becase otherwise we'd double
count)
To get how many multiples exists, a simple division is enough
To get the sum, we use a ArithmeticProgression
Sum(3 * 1..QT_MULTIPLES), where we can do:
3 * SUM(1..QT_MULTIPLES)
"""


def sum_multiples(number, upper_bound):
    qt_divisors = int(upper_bound / number)
    s = number * (qt_divisors * (qt_divisors + 1)) / 2
    return int(s)


answer = sum_multiples(3, 999) + \
         sum_multiples(5, 999) - \
         sum_multiples(15, 999)

print(answer)
"""
Another approach to this problem is -

1.Make an empty list
2.iterate between 0 to 1000 and find all the numbers which are divisible by either 3 or 5.
"""
l=[]
for i in range(0,1000):
  if i%3==0 or i%5==0:
    l.append(i)
print(sum(l))
