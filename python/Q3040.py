nums = list([int(input()) for i in range(9)])
tot = sum(nums)

for i in range(8):
    for j in range(i+1, 9):
        if(nums[i]+nums[j] == tot - 100):
            nums.pop(j)
            nums.pop(i)
            break
    if(sum(nums) == 100):
        break

for i in nums:
    print(i)