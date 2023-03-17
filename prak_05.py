def bubble_sort(array_data):
    n = len(array_data)
    for i in range(n):
        for j in range (n-i-1):
            if array_data[j] > array_data[j+1]:
                print(array_data)
                array_data[j], array_data[j+1] = array_data[j+1], array_data[j]
    return array_data
data = [81,94,39,93,67,28,11]
print(bubble_sort(data))