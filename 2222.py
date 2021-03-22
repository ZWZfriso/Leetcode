casest = input()
for _ in range(caset):
    lennums = input()
    nums = map(int, input().split(' '))
    count = 0
    while len(nums) != 0:
        mingn, mingi = max(nums), nums.index(max(nums))
        count += mingn
        frienda = (mingi - 1)%len(nums)
        friendb = (mingi + 1)%len(nums)
        nums.remove(mingn)
        nums.remove(nums[frienda])
        nums.remove(nums[friendb])
    print(count)