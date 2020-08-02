import re
handle=open('regex_sum_780916.txt')
sumNums=0
for line in handle:
    numList=re.findall('[0-9]+',line)
    for nums in numList:
        sumNums+=int(nums)
print(sumNums)