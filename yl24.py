# yl24

# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

# UPC vöötkoodi kontrollsumma arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri kontrollsumma arvutamise funktsioon. (https://www.w3schools.com/python/python_functions.asp)

""" 
The 12th digit (4 in this case) is a redundant check digit, used to catch errors. 
Using some simple calculations, a scanner can determine, given the first 11 digits, 
what the check digit must be for a valid code. 
(Check digits have previously appeared in this subreddit: see Intermediate 30 and Easy 197.) 
UPC's check digit is calculated as follows (taken from Wikipedia):

Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). 
If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).

Multiply the result from step 1 by 3.

Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, 
and add this sum to the result from step 2.

Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it M.

If M is 0, then the check digit is 0; otherwise the check digit is 10 - M.

For example, given the first 11 digits of a UPC 03600029145, you can compute the check digit like this:

Sum the odd-numbered digits (0 + 6 + 0 + 2 + 1 + 5 = 14).

Multiply the result by 3 (14 × 3 = 42).

Add the even-numbered digits (42 + (3 + 0 + 0 + 9 + 4) = 58).

Find the result modulo 10 (58 divided by 10 is 5 remainder 8, so M = 8).

If M is not 0, subtract M from 10 to get the check digit (10 - M = 10 - 8 = 2).

So the check digit is 2, and the complete UPC is 036000291452.

Challenge
Given an 11-digit number, find the 12th digit that would make a valid UPC. 
You may treat the input as a string if you prefer, whatever is more convenient. 
If you treat it as a number, you may need to consider the case of leading 0's to get up to 11 digits. 
That is, an input of 12345 would correspond to a UPC start of 00000012345.

Examples
upc(4210000526) => 4
upc(3600029145) => 2
upc(12345678910) => 4
upc(1234567) => 0 
"""

# 12 nr, 1,3,5 ...11 liidad (pos [0][2]), tulemuse korrutad 3-ga, liida sellele 2,4,6 jne nr summa, 
# leia 10-ga jagamise jääk (modulo) M. Kui M == 0, kontrollarv = 0, muul juhul kontrollarv = 10-M
# kui UPC nr lühem kui 11, lisada ette nulle

def find_check_digit(upc):
    #print (type(upc))
    upc = str(upc)
    if len(upc) != 11:
        upc = (upc).zfill(11)
    #print(upc)
    
    odd_digits = ""
    odd_digits += (upc[0:11:2])
    #print (odd_digits)
    sum_odd = 0
    for digit in odd_digits:
        sum_odd += int(digit)
    #print ("Sum odd " + str(sum_odd))
    
    even_digits = ""
    even_digits += (upc[1:11:2])
    #print (even_digits)
    sum_even = 0
    for digit in even_digits:
        sum_even += int(digit)
    #print ("Sum even " + str(sum_even))

    M = ((sum_odd*3) + sum_even) % 10
    if M == 0:
        print ("Kontrollnumber on " + str(M))
    else:
        check_digit = 10 - M
        print("Kontrollnumber on " + str(check_digit))


find_check_digit(1234567)

     