superheros_set = {"Avengers", "SuperMan", "SpiderMan"}
superheros_set.add("Iron Man")
superheros_set.add("Captain America")
superheros_set.add("Hulk")
superheros_set.add("Avengers") # Duplicates are not added to sets
print(superheros_set)

tamilheros_set = {"Rajni", "Kamal", "Vijay", "Ajith", "Vsethupadhi", "Dhanush", "Surya", "Simbu", "Hulk"}
print("union - ", superheros_set.union(tamilheros_set))
print("intersection -", superheros_set.intersection(tamilheros_set))

superheros_set.update({"Kamal", "Rajni", "Vijay"})
print("symmetric difference - ", superheros_set.symmetric_difference(tamilheros_set))


old_set = superheros_set.symmetric_difference(tamilheros_set)
print("old set : ",old_set)

new_set = superheros_set.symmetric_difference_update(tamilheros_set)
print("new set : ", new_set)

print(superheros_set.union(tamilheros_set).issuperset(tamilheros_set))
print(superheros_set.intersection(tamilheros_set).issubset(tamilheros_set))
