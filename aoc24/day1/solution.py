from collections import Counter


def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures fir for the task
    nums1, nums2 = [], []
    for line in lines:
        n1, n2 = line.split("   ")
        nums1.append(int(n1))
        nums2.append(int(n2))
    return nums1, nums2


def solve_part1(nums1: list[int], nums2: list[int]):
    # computes distances between sorted arrays
    nums1.sort()
    nums2.sort()
    ans = 0
    for n1, n2 in zip(nums1, nums2):
        ans += abs(n2 - n1)
    return ans


def solve_part2(nums1: list[int], nums2: list[int]):
    counter2 = Counter(nums2)
    ans = 0
    for num in nums1:
        ans += num * counter2[num]
    return ans
