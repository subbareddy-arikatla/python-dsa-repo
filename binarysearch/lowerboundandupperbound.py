def lowerbound(nums,taget):
  l=0
  h=len(nums)
  ans=len(nums)
  while(l<=h):
    m=(l+h)//2
    if(nums[m]>=target):
      ans=mid
      h=mid-1
    else:
      l=m+1
  return ans
  
  def upperbound(nums,taget):
  l=0
  h=len(nums)
  ans=len(nums)
  while(l<=h):
    m=(l+h)//2
    if(nums[m]>target):
      ans=mid
      h=mid-1
    else:
      l=m+1
  return ans