

def nums_generator(n):
   for num in range(1, n + 1, 2):
       yield num


nums_gen = nums_generator(10)

print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))


