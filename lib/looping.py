#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for n in range(10):
        print(n+1)
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared_list = list()
    for i in int_list:
        squared_list.append(i*i)
    return squared_list

def fizzbuzz():
    # code goes here!
    for i in range(100):
        n=i+1
        if(n%3==0):
            print("FizzBuzz") if n%5==0 else print("Fizz")
        else: 
            print("Buzz") if n%5==0 else print(n)
