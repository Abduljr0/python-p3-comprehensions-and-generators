#!/usr/bin/env python3

def return_evens(num_list):
    
    even_list=[x for x in num_list if x%2==0]

    print(even_list)
    return even_list
return_evens([0,2,3,4,5,6,7,9,8,10,12,24])

    




def make_exclamation(sentence_list):
    exclamation_list=[ (x+"!") for x in sentence_list ]

    print(exclamation_list)
    return exclamation_list

make_exclamation(["Hello","My name is","Abdul"])