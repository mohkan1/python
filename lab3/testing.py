import numpy as np

def powers(data, a, b):
    
    result = []
    result_row = []

    for number in data:
        for ex in range(a, b+1):
            result_row.append(number**ex)
        result.append(result_row)
        result_row = []
    return np.array(result)
    


print(powers([2,3,4],0,2))