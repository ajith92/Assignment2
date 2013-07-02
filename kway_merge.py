def heapify(nums,parent):
    if 2*parent+1<len(nums):
        if 2*parent+2<len(nums):
            if nums[2*parent+1]>nums[2*parent+2]:
                if nums[2*parent+1]>nums[parent]:
                    nums[parent],nums[2*parent+1]=nums[2*parent+1],nums[parent]
                    nums=heapify(nums,2*parent+1)
                else: return nums
            else:
                if nums[2*parent+2]>nums[parent]:
                    nums[parent],nums[2*parent+2]=nums[2*parent+2],nums[parent]
                    nums=heapify(nums,2*parent+2)
                else: return nums
        else:
            if nums[2*parent+1]>nums[parent]:
                    nums[parent],nums[2*parent+1]=nums[2*parent+1],nums[parent]
                    nums=heapify(nums,2*parent+1)
            else: return nums
    return nums

def kway(heap_list,original_pos,input_list,index,kway_sorted):
  while True:
		kway_sorted.append(heap_list[0])
		poped_index=original_pos.index(heap_list[0])			#index of the sublist	
		index[poped_index]+=1
		if index[poped_index]<len(input_list[poped_index]):
			original_pos[poped_index]=input_list[poped_index][index[poped_index]]
			heap_list[0]=input_list[poped_index][index[poped_index]]
			heap_list=heapify(heap_list,0)
		else:
			heap_list.remove(heap_list[0])
			original_pos[poped_index]=None
			
		if len(heap_list)<=0:
			return kway_sorted
		else:
			for i in range((len(heap_list)/2)-1,-1,-1):
            			heap_list=heapify(heap_list,i)
		
if __name__=='__main__':

	input_list=[[28,8,5,2],[23,21,17,11,10,12],[18,11,9,6],[],[92,30,26]]		#input should be sorted decsendingly
	#input_list=[[2],[6],[9],[],[8]]
	print input_list
	
	index=[]						#index to be concidered within the sublist
	for i in range(len(input_list)):
		index.append(0)
	
	original_pos=[]
	for i in range(0,len(input_list)):
		if len(input_list[i])>0:
			original_pos.append(input_list[i][index[i]])
		else:
			original_pos.append(None)
		
	heap_list=list(original_pos)
	for i in range(len(heap_list)/2-1,-1,-1):
		heap_list=heapify(heap_list,i)
			
	kway_sorted=[]
	kway_sorted=kway(heap_list,original_pos,input_list,index,kway_sorted)
	print kway_sorted
