'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    single_number = arr[0]

    for i in range(1, len(arr)):
        single_number ^= arr[i] 
    
    return single_number
    
    # for num in (arr):
    #     if arr.count(num) == 1:
    #         return num
    
    # data = {}
    # for num in arr:
    #     if num in data:
    #         data[num] += 1
    #     else:
    #         data[num] = 1

    # for (key, value) in data.items():
    #     if value < 2:
    #         return key

    # return None

    # res = arr[0]

    # for i in range(1, len(arr)):
    #     res = res ^ arr[i]
    # return res

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")