try:
     x = int(input())
     y = int(input())
     
     def gcd (a, b):
          while a != 0 and b != 0:
               if a > b:
                    a = a % b
               else:
                    b = b % a
          return a+b
     
          
     print (gcd(x, y))
          
     

except:
    print ('Как дела?') 

