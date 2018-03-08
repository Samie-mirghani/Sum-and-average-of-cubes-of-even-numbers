#Original Project2.py
#Shamsadean Mirghani
#This program will compute and display the sum and average
#of the cubes of the even natural numbers between 2 and n.
#n will be entered by the user


def main():

    # Handshake
    print("This program will compute and display the cubes and the")
    print("averages of natural numbers between 2 and n")
    # Checking the entry to make sure it is not below 2
    n=0
    while True:
        n = eval(input("please enter the value above 2 for n : "))
        if n >= 2:
            break
        else:
            print("Invalid Number")
    # Created empty list to store the even number
    even_number = []
    # Identifying the even numbers and adding them to the list        
    i=2
    for i in range (i, n+1):
        if i%2 == 0:
            even_number.append(i)
    # Count of even numbers in the list
    number_in_list = int(n/2)
    # Created new empty list to store the cubed numbers
    cubes = []
    # Computing cubes
    i=0
    for i in range (i, number_in_list):
        cube = even_number [i]**3
        cubes.append(cube)
    # Creating a value for Sum and summing the numbers from the cube
    # list
    Sum=0
    i=0
    for i in range (i, number_in_list):
        Sum= Sum+cubes[i]
    # Averaging the numbers in the cube list
    average=Sum/number_in_list
    # Printing the Sum and the Average of the cubes
    print('Sum= ',Sum, ' Average=', average)
    
  
main()
