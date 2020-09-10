import sys


def digit_sort(nums):
    max_len = max(len(n) for n in nums)
    for i in range(max_len - 1, -1, -1):
        digit_list = [list() for _ in range(10)]
        for n in nums:
            if len(n) > i:
                digit_list[int(n[i])].append(n)
            else:
                digit_list[int(n[0])].append(n)
        nums = [n for num_list in digit_list for n in num_list]
    for i in range(1, len(nums)):
        if abs(len(nums[i]) - len(nums[i - 1])) == 1 and \
            len(nums[i]) > len(nums[i - 1]) and \
                nums[i][-1] == nums[i - 1][0] and \
                nums[i][:-1] == nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums


def largest_number(a):
    a = digit_sort(a)
    return "".join(a[::-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
