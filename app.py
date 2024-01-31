

def number_prime():

    user_number = input("Enter a number: ")
    if(user_number.lower() == "stop"):
        return print("Finish..")
    user_number = int(user_number)

    if  user_number <= 1:
        print(user_number, "is not a prime number")
    else:
        is_prime = True
        for i in range(2, user_number):
            if user_number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(user_number, "is a prime number")
        else:
            print(user_number, "is not a prime number")
    number_prime()



# number_prime()

print("-------------------")

# ##

def terms_fibonacci():

  nterms = int(input("How many terms? "))
  
  # first two terms
  n1, n2 = 0, 1
  count = 0
  
  # check if the number of terms is valid
  if nterms <= 0:
     print("Please enter a positive integer")
  # if there is only one term, return n1
  elif nterms == 1:
     print("Fibonacci sequence: ")
     print(n1)
  # generate fibonacci sequence
  else:
     print("Fibonacci sequence:")
     while count < nterms:
         print(n1)
         if(n1 > nterms):
           print("Stop..")
           break
         nth = n1 + n2
         n1 = n2
         n2 = nth
         count += 1

# terms_fibonacci()
         

# ##
import re


def count_words_in_sentence():
    sentence = input("Insert a sentence: " )
    
    if(sentence == ""):
        return print(0)
    # split on white-space 
    word_list = re.split(r"\s+", sentence)
    print(len(word_list))

# count_words_in_sentence()

###
    




def print_factorial_numbers():

    number = input("Insert a number: ")
    if(not number.isnumeric()):
        print('Please insert a number')
        print_factorial_numbers()
    if (int(number) < 1):
        print('Please insert a number major than 0')
        return print_factorial_numbers()
    if(number.isnumeric()):
      number = int(number)
      fact = 1
      for num in range(2, number + 1):
        fact *= num
        print(fact)
      return fact
    else:
        print('Please insert a number')
        print_factorial_numbers()

num = print_factorial_numbers()

print("Result of factorial: ", num)

### 
        
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
    
# print(factorial(10))

def factorial2(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# print(factorial2(5))

