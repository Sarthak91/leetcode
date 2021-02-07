class TwoSum:
    def __init__(self, arr , target: int) :

        self.arr = arr
        self.target = target

    def get_to_sum(self):
        i = 0
        while i<len(arr):
            val = target - arr[i]
            if val in arr[i+1:]:
                return [i, arr.index(val, i+1)] 
            else:
                i += 1

                
        
if  __name__ == "__main__":
    arr = [3,2,4]
    target = 6
    two_sum = TwoSum(arr=arr, target=target) 
    print(two_sum.get_to_sum()) # [1,2]

    
