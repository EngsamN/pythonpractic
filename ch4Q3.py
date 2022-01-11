personsInvit = input("please enter number of  the person you want to invit them:")
if(int(personsInvit)<10):
    for i in range(10):
        personName= input("please enter name of  the person you want to invit them:")
        print("{0} has been invited ".format(personName))
elif(int(personsInvit)>=10):
    print("Sorry ,they will be  Too many people:(")





