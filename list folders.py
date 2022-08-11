import os 
my_list = os.listdir('')

# print ("The original list is : " + str(my_list))

for i in range(len(my_list)):
    print(my_list[i] , sep = "\n")