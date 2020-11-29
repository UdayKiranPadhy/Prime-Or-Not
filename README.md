# Prime Or Not

Date:-11/29/2020
Time:-4:11 PM

Check if a given number is Prime or Not .

A prime number is a whole number greater than 1, which is only divisible by 1 and itself. First few prime numbers are : 2 3 5 7 11 13 17 19 23 …..

How we check whether a number is Prime or not? 

Upto this level the problem of finding weather a given number is prime or not was just a whole problem or a huge part of a problem , but as the standards of competative programming increases it proposes a huge problem in the area of time complexity. I mean for example we want the sum of prime numbers upto 10000 suppose, then iterating from 1 to 10000 and checking each and every singlr number weather it is prime or not up to 10000, and even inside the prime we keep another For loop from 1 to some range so just imagine how much huge amount of calculations are being done , so it poses a problem .Same as you , I googled it out and spent some time in it , and found these.

1)Naive solution. 

A naive solution is to iterate through all numbers from 2 to n-1 and for every number check if it divides n. If we find any number that divides, we return false.

This is a Python Code by the way and has been taken from Geeks and Geeks site
```
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True
 

if isPrime(11):
    print("true")
else:
    print("false")
```
Bla Bla Bla .. Time Complexity O(n)

2) Naive Solution in few steps :

This solution is used for fewer no. of steps as compared to The solution above i.e square root( n)

```
import math
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, int(math.sqrt(n) +1)):
        if (n % i == 0):
            return False
 
    return True
 

if isPrime(11):
    print("true")
else:
    print("false")
```


Can't we find weather a number is prime or not just by looking at it , i mean to say not by iterating all the numbers upto sqrt of n ??
The Answer is Both Yes And No.

Ok take a break from the code , and some theory part here
I found that every prime number over 3 lies next to a number divisible by six.  Using Matlab with the help of a friend, we wrote a program to test this theory and found that at least within the first 1,000,000 primes this holds true.

Checking a million primes is certainly energetic, but it is not necessary (and just looking at examples can be misleading in mathematics). Here is how to prove your observation: take any integer n greater than 3, and divide it by 6.  That is, write
```
n = 6q + r
```
where q is a non-negative integer and the remainder r is one of 0, 1, 2, 3, 4, or 5.

```
<ul>
<li>If the remainder is 0, 2 or 4, then the number n is divisible by 2, and can not be prime.</li>
<li>If the remainder is 3, then the number n is divisible by 3, and can not be prime.</li>
</ul>
```

So if n is prime, then the remainder r is either
```
<ul>
<li>1   (and   n = 6q + 1   is one more than a multiple of six), or </li>
<li>5   (and   n = 6q + 5 = 6(q+1) - 1   is one less than a multiple of six). </li>
</ul>
```

2   3  4  5  6  7<br>
8   9 10 11 12 13<br>
14 15 16 17 18 19<br>
20 21 22 23 24 25<br>
26 27 28 29 30 31<br>
32 33 34 35 36 37<br>
38 39 40 41 42 43<br>
44 45 46 47 48 49<br>
50 51 52 53 54 55<br>
56 57 58 59 60 61<br>
62 63 64 65 66 67<br>
68 69 70 71 72 73<br>
74 75 76 77 78 79<br>
80 81 82 83 84 85<br>

As we see the 4th and 6th column(number count starting from 1 not from 0) most of them are prime and are next or preciding to 6 table (5th row) .

Remember that being one more or less than a multiple of six does not make a number prime.  We have only shown that all primes other than 2 and 3 (which divide 6) have this form.

Taking the example of number 25 and 35 tells that every prime number expt 2 and 3 is of the form 6q -+ 1 but not every number of 6q -+ 1 is prime. 

So the optimum Solution is looks something this.

```
def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    if (n % 6 == 1) or (n % 6 == 5):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    return False
```

So coming back to the question .

Can't we find weather a number is prime or not just by looking at it , i mean to say not by iterating all the numbers upto sqrt of n ??

Hope you got the answer.

And is this is the most optimum solution ?
No its just easy to write and remember the code not the optimum once.

You can futher optmize it by Reducing the number of iterating steps in the for loop.
Actually u just need to check the divisiblity of all primes below sqrt(n) + 1 , not all the number below it.
