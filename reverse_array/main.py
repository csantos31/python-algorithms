from time import sleep

def main(): 
    array_to_reverse = ['item1', 'item2', 'item3', 'item4', 'itemN']
    print_array('Original Items', array_to_reverse)
    
    result = reverse_array(array_to_reverse)
    sleep(1)    
    print_array('Reversed Items', result)
    
    
def reverse_array(array):
    result_array = array
    middle_len = len(array) // 2
    
    for i in range(middle_len):
        aux = result_array[i]
        result_array[i] = result_array[len(result_array)-i-1]
        result_array[len(result_array)-i-1] = aux

    return result_array


def print_array(description, array):
    print(f'{description}: ', end=' => | ')
    for item in array:
        print(item, end=' | ')
    print('\n--------------------------------------------')

main()

