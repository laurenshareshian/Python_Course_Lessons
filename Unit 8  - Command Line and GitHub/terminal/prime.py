def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
   n = int(input('Gimme a number: ' ))
   print(is_prime(n))

if __name__ == '__main__':
   main()




