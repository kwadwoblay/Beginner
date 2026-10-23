# Sum of N Natural Numbers
N = int( input('Enter the value of N: '))
sum_ = 0
for i in range(1, 1+N):
    sum_ = sum_ + i

print(f'The sum of the first {N} natural numbers is {sum_}')

