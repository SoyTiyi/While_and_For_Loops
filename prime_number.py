def is_diveder(a,b):
    if(a % b == 0):
        return True
    return False

def prime_number(number):
    index = 1
    cont_dividers = 0
    while(index <= number / 2):
        if(is_diveder(number,index)):
            cont_dividers += 1
        index += 1
    cont_dividers += 1
    if(cont_dividers == 2 or number == 1):
        print("This number is a prime number")
    else:
        print("This number is not a prime number")

def main():
    number = input("Enter a number: ")
    prime_number(int(number))

if __name__ == "__main__":
    main()


