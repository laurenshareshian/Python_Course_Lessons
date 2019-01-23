def is_even(i):
   ''' this function returns True if i is even and False otherwise'''
   ###put stuff here
   if i % 2 == 0:
      return True
   else:
      return False


def main():
   n = int(input('Gimme a max number: '))
   for i in range(n+1):
      if is_even(i):
          print(i)

if __name__ == '__main__':
   main()








