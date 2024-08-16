mmutable_var = 5, "snob", False, 1.5
print(mmutable_var)
print (mmutable_var[1])
print (mmutable_var[2:5])
# mmutable_var[1] = 'g' нельзя изменить кортеж
mutable_list = ['a', 'b', 'c', 'd']
mutable_list[3] = 'w'
print(mutable_list)