from math import factorial
import sys
from collections import defaultdict

fl = {}
facts = defaultdict(lambda:0)
def calc(n):
    global fl
    a = []
    for i in range(n+1):
        k = fl.get((n,i), None)
        if k is not None:
            sys.stdout.write(k)
            sys.stdout.write(' ')
        else:
            a = facts[n]
            b = facts[i]
            c = facts[n-i]

            if a == 0:
                a = factorial(n)
                facts[n] = a
                
            if b == 0:
                b = factorial(i)
                facts[i] = b

            if c == 0:
                c = factorial(n-i)
                facts[n-i] = c
            
            f = a/(b*c)

            if f > 1000000000:
                f = f % 1000000000
            fl[(n,i)] = str(f)
            sys.stdout.write(fl[(n,i)])
            sys.stdout.write(' ')
    print ''    

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        calc(int(raw_input()))