"""def find_sum(nums,key):
	i=0
	while i<len(nums) and nums[i]<key:
		low=i+1
		high=len(nums)-1
		while low<=high:
			mid=(low+high)/2
			if nums[i]+nums[mid]==key:
				print "Found a pair with index : ",i,mid
				return
			elif nums[i]+nums[mid]>key:high=mid-1
			else:low=mid+1
		i+=1
	print "No such pair found" """
				
def find_sum(nums,key):
	s=0
	e=len(nums)-1
	while s<e:
		if nums[s]+nums[e]==key :
			print "Such pair found at index ("+str(s)+","+str(e)+")"
			print "nums["+str(s)+"] = "+str(nums[s])
			print "nums["+str(e)+"] = "+str(nums[e])
			print str(nums[s])+"+"+str(nums[e])+"="+str(key)
			return
		elif nums[s]+nums[e]<key :
			s+=1
		else : 
			e-=1
	print "No such element found"


def get_data():
        nums=[]
        while True:
            a=int(raw_input("Enter a number (-1 if done) : "))
            if a==-1:
                break
            nums.append(a)
        return nums

if __name__=='__main__':
        print "Enter a list : "
	nums=get_data()
        nums.sort()
	print "list data is : ",nums
        key=int(raw_input("Enter the key : "))
	find_sum(nums,key)
