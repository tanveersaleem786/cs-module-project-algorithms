'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    count = 0
    rslt_arr = [0]*len(arr)
    for i in range(0, len(arr)):
        if arr[i] != 0:            
            rslt_arr[count] = arr[i]
            count += 1
    
    return rslt_arr

    # count = 0
    # total = len(arr)   
    # for i in range(0, total):
    #     if arr[i] != 0:
    #         arr[count] = arr[i]
    #         count += 1

    # while count < total:
    #     arr[count] = 0
    #     count += 1    
    # return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")