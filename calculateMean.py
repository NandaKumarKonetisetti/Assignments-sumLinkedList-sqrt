
def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data =list(map(int,input("Enter a numbers to calculate the mean ").split()))
mean_value = calculate_mean(data)
print("Mean:", mean_value)
