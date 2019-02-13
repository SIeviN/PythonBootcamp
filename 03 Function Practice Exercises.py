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

#######################################################################################################################################################################
print(' ')
print('7.')
print('FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.')
#######################################################################################################################################################################

def has_33(nums):
    prev = 0
    for i in nums:
        if i == 3 and i == prev:
            return True
        else:
            prev = i
    return False

print('has_33([1, 3, 3]) = ', has_33([1, 3, 3]))
print('has_33([1, 3, 1, 3]) = ', has_33([1, 3, 1, 3]))
print('has_33([3, 1, 3]) = ', has_33([3, 1, 3]))

#######################################################################################################################################################################
print(' ')
print('8.')
print('PAPER DOLL: Given a string, return a string where for every character in the original there are three characters')
#######################################################################################################################################################################

def paper_doll(text):
    newstring = ''
    for i in text:
        newstring += i*3
    return newstring

print('paper_doll(Hello) = ', paper_doll('Hello'))
print('paper_doll(Mississippi) = ', paper_doll('Mississippi'))

#######################################################################################################################################################################
print(' ')
print('9.')
print('BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.')
print('If their sum exceeds 21 and theres an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return BUST')
#######################################################################################################################################################################

def blackjack(a,b,c):
    tot = a+b+c
    if tot <= 21:
        return tot
    elif tot > 21:
        if a == 11 or b == 11 or c == 11:
            tot -= 10
            if tot > 21:
                return 'BUST'
            else:
                return tot
        else:
            return 'BUST'

print('blackjack(5,6,7) = ', blackjack(5,6,7))
print('blackjack(9,9,9) = ', blackjack(9,9,9))
print('blackjack(9,9,11) = ', blackjack(9,9,11))

#######################################################################################################################################################################
print(' ')
print('10.')
print('SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and')
print('extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.')
#######################################################################################################################################################################

def summer_69(arr):
    sixflag = 0
    tot = 0
    for i in arr:
        if sixflag == 0 and i != 6 and i != 9:
            tot += i
        elif i == 6:
            sixflag = 1
            continue
        elif i == 9 and sixflag == 1:
            sixflag = 0
            continue
    return tot

print('summer_69([1,3,5]) = ', summer_69([1,3,5]))
print('summer_69([4, 5, 6, 7, 8, 9]) = ', summer_69([4, 5, 6, 7, 8, 9]))
print('summer_69([2, 1, 6, 9, 11]) = ', summer_69([2, 1, 6, 9, 11]))

#######################################################################################################################################################################
print(' ')
print('11.')
print('SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order')
#######################################################################################################################################################################

def spy_game(nums):
    fzero = 0
    szero = 0
    for i in nums:
        if i == 0 and fzero == 0:
            fzero = 1
        elif i == 0 and fzero == 1 and szero == 0:
            szero = 1
        elif i == 7 and fzero == 1 and szero == 1:
            return True
    return False

print('spy_game([1,2,4,0,0,7,5]) = ', spy_game([1,2,4,0,0,7,5]))
print('spy_game([1,0,2,4,0,5,7]) = ', spy_game([1,0,2,4,0,5,7]))
print('spy_game([1,7,2,0,4,5,0]) = ', spy_game([1,7,2,0,4,5,0]))

#######################################################################################################################################################################
print(' ')
print('12.')
print('COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number')
#######################################################################################################################################################################

def count_primes(num):
    count = 0
    for i in range(2,101):
        if i%2 != 0 and i%3 != 0 and i%5 !=0 and i%7 != 0:
            count += 1
        if i == 2 or i == 3 or i == 5 or i == 7:
            count += 1
    return count

print('count_primes(100) = ', count_primes(100))