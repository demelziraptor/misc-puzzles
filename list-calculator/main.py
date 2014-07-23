# possible values for each list item
nums = range(48,91)
# size of the list
list_size = 5
# calculation target for a list
target = 2308
# list of lists that meet the target
options = []

def calculation(num_list):
    """ performs required calculation on the list """
    num_start = 3
    result = 0
    for i in num_list:
        result += i * num_start
        num_start += 1
    return result

def reduce_counter(counter):
    """ reduces the counter, or if it's empty returns false """
    if not sum(counter):
        return False
    for i,val in enumerate(counter[::-1]):
        reali = len(counter) - (i+1)
        if val:
            counter[reali] = val - 1
            return counter
        counter[reali] = len(nums) - 1

def build_counter():
    """ set up the initial counter """
    counter = []
    max_num = len(nums) - 1
    for i in range(list_size):
        counter.append(max_num)
    return counter

# create counter and do calculation until the counter runs out!
counter = build_counter()
while counter:
    num_list = [nums[i] for i in counter]
    if calculation(num_list) == target:
        options.append(num_list)
    counter = reduce_counter(counter)

# the end
if not options:
    print "Nothing :("
    exit(0)
print str(options)
