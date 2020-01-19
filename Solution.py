def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) -1] == 6:
        return True
    else:
        return False


def same_first_last(nums):            
    if len(nums) >= 1:
        if nums[0] == nums[len(nums) -1]:
            return True
        else:
            return False
    else:
        return False 

def make_pi():
    return [3, 1, 4] 

def common_end(a, b):
    return (a[0] == b[0]) or (a[len(a) -1] == b[len(b) -1])

def sum3(nums):
    return nums[0] + nums[1] + nums[2]


def rotate_left3(nums):
    """ result = [] 
    result.append(nums[1])
    result.append(nums[2])
    result.append(nums[0]) """
    return [nums[1], nums[2], nums[0]]    # result


print(rotate_left3([1, 2, 3]))    


def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


def max_end3(nums):
    if nums[0] >= nums[2]:
        return [nums[0], nums[0], nums[0]]
    else:
        return [nums[2], nums[2], nums[2]]


def sum2(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]  


def middle_way(a, b):
    return [a[1], b[1]]
    

def make_ends(nums):
    return [nums[0], nums[len(nums) -1]]

def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3    


print(has23([2, 5]))    