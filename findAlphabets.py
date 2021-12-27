
## code to find the number of occurences of an alphabet in a list

words = ["do", "was", "numnber", "order", "apple", "organe", "elephant"]
find = input("Enter the alpabet that you want to find\n")
count = 0
for word in words:
    if not type(word) is str:
        continue;
    else:
        lst = list(word)
        count = count + lst.count(find)

print("Total occurence : ", count)