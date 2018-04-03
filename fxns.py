def odd_even(x):
    i = 0
    while i <= x:
        if i%2==0:
            print "Number is", i, "This is an even number"
        else:
            print "Number is", i, "This is an odd number"
        i+=1

odd_even(2000)

def multiply_by_five(arr):
    for number in range(len(arr)):
        arr[number] = arr[number] * 5
    print arr

multiply_by_five([1,2,3,4,5])


# Returns array with values multiplied by 5 and prints number 1-2000 while saying if it's odd or even