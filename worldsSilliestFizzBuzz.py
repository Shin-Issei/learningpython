# Yes that filename is abosolutley correct



nums = []
for i in range(1000):
    nums.append(i)

def doDaFizzBuzz(numberArray):
    for i in numberArray:
        if (i % 3 == 0):
            print("Fizz")
            
        if (i % 5 == 0):
            print("Buzz")

        if((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz")
        else:
            print(i)

doDaFizzBuzz(nums)

# i = 15

# if(i % 3 == 0 and i % 5 == 0):
#     print("That's true")

# else:
#     print("Bro nah.")

'''
TL:DR CODE WHEN PISSED OFF ALSO:
REMEMBER: the continue statement means that all code underneath gets skipped. 

As it turns out that filename wasn't all that correct after all. 
The more important thing is that I am not freaking out anymore about the 
insult I suffered at the hands of my cunt supervisor.
As it turns out, of all things thinking logically and making the 
things that I am intrested in calms me down even more that I would have dreamed
This is great. No matter what happens and no matter how pissed off I am I think
I might be able to code something simple and solve a little problem for myself
and make my self feel better. 

An explanation for the bug in the fizzbuzz.

the continue statement was my short circuting my code by accident. What I was
forcing the code to do was to stop short at the first true statement
meaning that the other statements were not being checked.

'''