# -*- coding: utf-8 -*-
"""
#.##..###.#....#...####.#.
Created on Tue Jun 19 22:53:03 2018
@author: TLapP
Description: Tools to hide a number (most often your date of birth) in your scripts without being interpreted.
"""

def modify_the_number(number_to_hide):
    """
    Alters the number to hide. 
    This function allows everyone to have their own function so that others can not find the hide number.
    This function must be kept secret.
    """
    return number_to_hide*2

def reverse_modify_the_number(number_to_hide):
    """
    Reverse the modify function.
    This function must be kept secret.
    """
    return number_to_hide/2

def get_the_character(characters_list=[]):
    """
    Allows you to find the number escaped or the other number.
    """
    indice_character = 0
    last_character = characters_list[0]
    for character in characters_list:
        if character != last_character:
            break
        else:
            last_character = character
        indice_character += 1
    return ''.join(characters_list[:indice_character]), indice_character

def get_the_corresponding_character(characters_list=[], lenght_caracter=0):
    """ Allow to put the characters together so that they can match the escaped character or the other. """
    temporary_list=[]
    temporary_answer = []
    for character in characters_list:
        if len(temporary_list)<lenght_caracter-1:
            temporary_list.append(character)
        else:
            temporary_list.append(character)
            temporary_answer.append(temporary_list)
            temporary_list=[]
    answer = []
    for character_join in temporary_answer:
        answer.append(''.join(character_join))
    return answer

def generate_the_mark(number_to_hide, escaped_character, other_character):
    """ 
    Generate the mark that can be placed in the code.
    The characters escaped are the characters that the programming language does not interpret for example # in python or // for arduino.
    The length of the escaped character and that of the other character must be the same otherwise the function will return 0.
    """
    number_to_hide = modify_the_number(int(number_to_hide)) # Prefer: YearMonthDay
    bin_number = list(bin(number_to_hide)[2:])
    answer = [escaped_character]
    for character in bin_number:
        if character == "1":
            answer.append(other_character)
        else:
            answer.append(escaped_character)
    return ''.join(answer)

def decipher_the_mark(the_mark, escaped_character="", other_character=""):
    """ 
    Decipher the mark that has been placed in the code.
    The characters escaped are the characters that the programming language does not interpret for example # in python or // for arduino.
    The length of the escaped character and that of the other character must be the same otherwise the function will return 0.
    The escaped character and the other must be the same as those used to make the mark. 
    You do not have to specify the escaped character and the other character.
    """
    the_mark = get_the_corresponding_character(list(the_mark), len(escaped_character))
    indice_character = len(escaped_character)
    if not escaped_character:
        escaped_character, indice_character = get_the_character(the_mark)
        the_mark = get_the_corresponding_character(list(the_mark), len(escaped_character))
    else:
        if not other_character:
            other_character = the_mark[1]
    if not other_character:
        other_character, indice_character = get_the_character(the_mark[indice_character:])
        print(escaped_character, other_character, the_mark)
    answer = []
    for character in the_mark:
        if character == escaped_character:
            answer.append("0")
        elif character == other_character:
            answer.append("1")
    bin_number = ''.join(answer)
    return int(reverse_modify_the_number(int(bin_number, 2)))
                      