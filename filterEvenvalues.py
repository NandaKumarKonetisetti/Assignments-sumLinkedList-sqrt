def filterEvenNumbers(li):
    return [x for x in li if x%2==0]
values = list(map(int,input("Enter the  numbers ").split()))
print(filterEvenNumbers(values))