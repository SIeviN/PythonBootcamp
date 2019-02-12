#######################################################################################################################################################################
print(' ')
print('1.')
print('LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even')
print('but returns the greater if one or both numbers are odd')
#######################################################################################################################################################################

def lesser_of_two_evens(a,b):
    if a%2 != 0 or b%2 != 0:
        return max(a,b)
    else:
        return min(a,b)

print('lesser_of_two_evens(2,4) = ', lesser_of_two_evens(2,4))
print('lesser_of_two_evens(2,5) = ', lesser_of_two_evens(2,5))


#######################################################################################################################################################################
print(' ')
print('2.')
print('ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter')
#######################################################################################################################################################################

def animal_crackers(text):
    newtext = text.split()
    return newtext[0][0].lower() == newtext[1][0].lower()

print('animal_crackers(Levelheaded llama) = ', animal_crackers('Levelheaded llama'))
print('animal_crackers(Crazy Kangaroo) = ', animal_crackers('Crazy Kangaroo'))

#######################################################################################################################################################################
print(' ')
print('3.')
print('MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False')
#######################################################################################################################################################################

def makes_twenty(n1,n2):
    return (n1 == 20 or n2 == 20 or n1+n2 == 20)

print('makes_twenty(20,10) = ', makes_twenty(20,10))
print('makes_twenty(2,3) = ', makes_twenty(2,3)) 

#######################################################################################################################################################################
print(' ')
print('4.')
print('OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name')
#######################################################################################################################################################################

def old_macdonald(name):
    newname = ''
    for a,b in enumerate(name):
        if a == 0 or a == 3:
            newname += b.capitalize()
        else:
            newname += b
    return newname

print('old_macdonald(macdonald) = ', old_macdonald('macdonald'))

#######################################################################################################################################################################
print(' ')
print('5.')
print('MASTER YODA: Given a sentence, return a sentence with the words reversed')
#######################################################################################################################################################################

def master_yoda(text):
    newstring = text.split()
    newstring.reverse()
    return " ".join(newstring)

print('master_yoda(I am home) = ', master_yoda('I am home'))
print('master_yoda(We are ready) = ', master_yoda('We are ready'))

#######################################################################################################################################################################
print(' ')
print('6.')
print('ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200')
#######################################################################################################################################################################

def almost_there(n):
    return n in range(90,111) or n in range(190,211)

print('almost_there(104) = ', almost_there(104))
print('almost_there(150) = ', almost_there(150))
print('almost_there(209) = ', almost_there(209))








