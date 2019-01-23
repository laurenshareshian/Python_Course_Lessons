import prime

def main():
    #put stuff here. here's an example of how to call is_prime:
    n = int(input('Gimme a number: ' ))
    for i in range(2, n):
        if prime.is_prime(i):
             print(i)
if __name__ == '__main__':
    main()





