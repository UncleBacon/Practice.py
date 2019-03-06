
def odd_even():
    num = int(input("Enter a number:"))

    if num % 2==0:

        print(f"{num} is even.")

    else:

        print(f"{num} is odd.")

#odd_even()

def lessthan_ten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    myvar = int(input("Look for numbers less than: "))
  #  new_list = []
  #  if myvar < a in a:
  #      new_list.append(a)
  #      print(new_list)
    print([xx for xx in a if xx < myvar])
#lessthan_ten()

def divisors():
    y = int(input("Choose a number: "))
    p = []
    for i in list(range(1,y+1)):
        if y % i == 0:
            p.append(i)
    print(p)
#divisors ()

import random
def list_compare():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []

    for i  in b:
        if i in a:
            c.append(i)
    print(c)


#list_compare()

import random
def list_compare2():
    a = []
    b = []
    c = []
    for i in range(random.randint(0,100)):
        a.append(random.randrange(0,100))
        b.append(random.randrange(0, 100))
    print(a)
    print(b)
    for i  in b:
        if i in a:
            c.append(i)
    if c == []:
        print("No Matches")
    else:
        print(c)


#list_compare2()

def string_list():
    a = input("Please provide a word:\n")
    b = a[::-1]
    print(b)
    if a == b:
        print("This is a Palindrome")
    else:
        print("Not a Palindrome...")

#string_list()



def even_list():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even = [aa for aa in a if aa % 2 == 0]
    print(even)
    #evens = []
    #for aa in a:
     #   if aa % 2 == 0:
     #       evens.append(aa)
    #print(f"The following numbers are even:\n {evens}")

#even_list()

import random
def RPS():
    call = ["rock", "paper", "scissors"]
    player = input( "Choose: Rock, Paper, or Scissors:\n ").lower()
    computer = call[random.randrange(0,3)]
    print(f" Player: {player.capitalize()}\n Computer: {computer.capitalize()}")
    if player == computer:
       print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print(f" {player.capitalize()} beats {computer.capitalize()}! Player wins!")
    elif player == "paper" and computer == "rock":
        print(f" {player.capitalize()} beats {computer.capitalize()}! Player wins!")
    elif player == "scissors" and computer == "paper":
        print(f" {player.capitalize()} beats {computer.capitalize()}! Player wins!")
    else:
        print(f"You lose. {computer.capitalize()} beats {player.capitalize()}.")

#RPS()

def guess():
        var1, var2 = [int(x) for x in input("Enter two numbers separated by a space: ").split()]
        comp = random.randint(var1,var2)
        g = 0
        c = 1
        while g != "exit" and g != comp:
            g = input("Please guess a number or type Exit to leave: ").lower()
            if g == "exit":
                print("Thanks for playing!")
                break
            g = int(g)
            if g != comp:
                print(f"{g} is wrong")
            elif g == comp:
                print(f"Congrats! You guessed right on try # {c}")
                break

            c += 1
#guess()

a = [random.randrange(1,999) for x in range(random.randint(1,999))]
b = [random.randrange(1,999) for x in range(random.randint(1,999))]

d = [1,2,3,4,5,6,7,8,9,0]
e = [14,1,5,6,7,12,11,11]

def overlap(x,y):
    c = []
    for xx in x:
        if xx in y:
            if xx not in c:
             c.append(xx)
    print(c, "\n")

    print("There are:", len(c), "elements in this array.")

#overlap(a,b)



def Primescomp():
    var = int(input("Please enter the number you want to check for prime: "))
    c = []
    d = []
    for x in range(2, var + 1):
        is_prime = True
        for y in range(2, int(x ** 0.5)+1):
            if x % y == 0:
                is_prime = False
            elif is_prime:
                c.append(x)
    for x in c:
        if x not in d:
            d.append(x)
        print(d)


#Primescomp()

def fib():
    a = int(input("How many numbers in the Fibonacci sequence would you like to see?"))

    b = int(input("What number would you like to start with?"))
    print(f"OK I will create a sequence {a} numbers long starting with {b}")
    c = []
    c.append(b)
    for x in range(0, a-1):
       if b == 0:
           b = b + 1
           c.append(b)
       elif len(c) == 1:
           b = b + (b-1)
           c.append(b)
       else:
              b = b + c[x-1]
              c.append(b)
    print(c)
#fib()


xx = [1,1,2,3,4,5,5,6,6,7,8,9,9,9,10]

def remDupe(x):
    Output =[]
    for i in x:
        if i not in Output:
            Output.append(i)
    print(Output)

#remDupe(xx)


xx = ["BB", "CC", "DD", "BB", "DD", "AA"]
def remDupeV2(x):

    print(set(x))

#remDupeV2(xx)

def back():
    y = input("Give me a sentence: ")
    z = y.split()
    print(' '.join(z[::-1]))

    #print(' '.join(((input("Give me a sentence :")).split())[::-1]))
    print(set(z))
    print(' '.join(set(z)))
#back()

