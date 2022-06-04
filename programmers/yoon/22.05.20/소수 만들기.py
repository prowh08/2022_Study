def solution(nums):
    prime=0
    arr=[]
    for i in range(0, len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                n = nums[i]+nums[j]+nums[k]
                cnt=0
                arr.append(n)
                for k in range(2,n):
                    if n%k==0:
                        cnt+=1
                if cnt<1:
                    prime+=1
    return prime