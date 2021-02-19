'''
Created on Feb 19, 2021

@author: logan
'''
import random

def swap(num1, num2):
    if num1 < num2:
        "yes"
    
def main():
    list = [random.randint(0, 100)] * random.randint(0, 100)
    compares = 0
    swaps = 0
    
    for i in range(len(list)-1):
        if i == 0:
            list[i] = list[i]
        else:
            if list[i] < list[i-1]:
                "yes"
if __name__ == '__main__':
    main()