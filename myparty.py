personslist = []
def party():
    personsInvit=input("please enter 3 names of  the person you want to invit them:").split()
    print((personsInvit))
    personslist.extend(personsInvit)
party()
askUser=input("if you want to invit another person print yes Or to exit print no?")
if(askUser=='yes'):
    while True:
        personsInvit = input("please enter name of  the person you want to invit them:").split()
        personslist.extend(personsInvit)
        askUser = input("if you want to exit print no and if you want to conutue invite person press enter key")
        if (askUser == 'no'):
            print('you invit {} persons'.format(len(personslist)))
            exit()

elif(askUser=='no'):
    print('you invit {} persons'.format(len(personslist)))

