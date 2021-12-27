##code to find the number of occurrence of a number in a list

elements = [11,2,123,34,34,4554,223,1,2,3,4,6,7,8,1,1,1,1,32,3,43,4,4,5]
id = int(input("enter the number you want to search in the list \n"))
count = 0
for element in elements:
    if not type(element) is int:
        continue;
    else:
        # lst = [int(x) for x in str(element)]
        # lst = list(element) --> this does not work here as int is not an iterable element
        lst = list(str(element))
        count = count + lst.count(str(id))

print("Total count :", count)
