###############
# Form 1.0
# Alex
###############

First_Name = input("what is your First Name : ").capitalize()
Last_Name = input("what is your Last Name : ").capitalize()
Age = input("How old are you (dd/mm/yyyy): ")



f = open(First_Name +" "+ Last_Name,'w')    #the First and Last name will be the txt file name
f.write('First name : '+ First_Name)
f.write('\nLast name : ' + Last_Name)
f.write('\nDate of Birth : ' + Age)


f.close()


