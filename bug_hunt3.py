def remove_negatives(numbers):
    
    positive_numbers = []    
    
    for num in numbers:
        if num >= 0:
            positive_numbers.append(num)
            
    return positive_numbers

print(remove_negatives ([1, -2, -3, 4, -5]))

