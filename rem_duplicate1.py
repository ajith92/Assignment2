def rem_duplicate(nums):
  i=0
	while i<len(nums):
		if i+1<len(nums) and nums[i]==nums[i+1]:	
			nums.remove(nums[i])
		i+=1
	return nums			

def quick_sort(nums,start,end):
	if start<end:
		p=start
		i=start	
		j=end
		while i<j:
			while nums[i]<=nums[p] and i<end:
				i+=1
			while nums[j]>nums[p]: 
				j-=1
			if i<j:
				nums[i],nums[j]=nums[j],nums[i]
		nums[p],nums[j]=nums[j],nums[p]
		quick_sort(nums,start,j-1)
		quick_sort(nums,j+1,end)					
	return nums			
	
def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 if done) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
	#collect data
	nums=get_data()
	#print input data
	print "Input data is : ",nums
	nums=quick_sort(nums,0,len(nums)-1)
	nums=rem_duplicate(nums)
	print "After removing duplicates : ",nums
 
