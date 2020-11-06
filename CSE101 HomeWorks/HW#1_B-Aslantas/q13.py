mylist = [1, 2, 3, 56, 708, 501]
print("mylist=", mylist)
input_num = int(input("Enter a number which is not in the list= "))
print(input_num, "in my list", input_num in mylist)
print(input_num, "not in my list", input_num not in mylist)