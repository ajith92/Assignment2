def rem_dupli(nums):
  new_list=[]
	for i in nums:
		if i not in new_list:
			new_list.append(i)
	return new_list


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
	print "Enter a list" 
	nums=get_data()
	#print input data
	print "Input data is : ",nums
	#remove duplicate
	nums=rem_dupli(nums)
	#print sorted data
	print "sorted data is : ",nums
