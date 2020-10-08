
def transpose(data):

    if len(data)>0:

        result = []
        result_row = []
        newResultRow = len(data[0])
        newResultCol = len(data)

        for row in range(newResultRow):
            for col in range(newResultCol):
                result_row.append(0)
            result.append(result_row)
            result_row = []
        

        for i in range(len(data)):
            for j in range(len(data[0])):
                result[j][i] = data[i][j]

        return result
    else:
        return []

def powers(data, a, b):
    
    result = []
    result_row = []

    for number in data:
        for ex in range(a, b+1):
            result_row.append(number**ex)
        result.append(result_row)
        result_row = []
    return result
    


def matmul(matrix, matrix1):

    if len(matrix)>0:
        result = []
        result_row = []
        newResultRow = len(matrix)
        newResultCol = len(matrix1[0])
        

        for row in range(newResultRow):
            for col in range(newResultCol):
                result_row.append(0)
            result.append(result_row)
            result_row = []

        for i in range(len(matrix)):
            for j in range(len(matrix1[0])):
                for k in range(len(matrix1)):
                    result[i][j] += matrix[i][k] * matrix1[k][j]
    else:
        return []

    return result


def invert(data):
    det = float(( data[0][0] * data[1][1] ) - ( data[0][1] * data[1][0] ))
    for row in range(len(data)):
        for col in range(len(data[row])):   
            data[row][col] /= det
    temp = data[0][0]

    data[0][0] = data[1][1]
    data[1][1] = temp

    data[0][1] *= -1
    data[1][0] *= -1
    return data


def loadtxt(name):
    f = open(name)
    data = f.read().splitlines()

    result = []

    for item in data:
        result.append(item.split("\t"))
    
    for row in range(len(result)):
        for col in range(len(result[row])):
            result[row][col] = float(result[row][col])

    return result
    
#print(loadtxt("chirps.txt"))
        
    
