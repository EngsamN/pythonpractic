'''  While the total is 50 or less, ask the user to input a number.
 Add that number to the total and print the message “The total is… [total]”.
  Stop the loop when the total is over 50. Upload program to GitHub and past the link.
'''
total=0
while total<=50:
    numb=int(input('Enter a number:'))
    total= total + numb
    print("the total is ",total)
    if(total>50):
        break




