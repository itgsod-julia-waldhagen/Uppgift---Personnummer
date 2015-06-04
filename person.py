__author__ = 'julia.waldhagen'
# -*- coding: utf-8 -*-



def valid_pnr(number):
    """
    Takes your (Swedish) personal number as a 11-digit string with a hyphen as the argument (for example: "xxxxxx-xxxx")
    Checks for letters or too many digits - if so, returns false
    Removes the last number of the argument and makes it the control number
    Every second digit is doubled into a new sum
    Takes every individual digit from each sum and adds to a final sum
    If the final sum plus the control number is evenly divisble with 10, returns true
    :param number:string
    :return:boolean
    """
    notnumbers = []
    #create an empty list for debugging
    if len(number) != 11:
        return False
        #if the length of the argument number is not 11
        #return False
    for position,num in enumerate(number):
        if not num.isdigit():
            notnumbers.append(num)
        #if the strings in number are not not digits
        #add to the list of non-digits
    while len(notnumbers) > 1:
            return False
        #if the list of non-digits is longer than 1
        #return False

    part1 = number.split("-")[0]
    part2 = number.split("-")[1]
    #split the number into two parts and remove the hyphen
    control = part2[3]
    part2 = part2.split(part2[2])[0] + part2[2]
    #separate the control number
    listofnum = []
    listofsum = []
    total = 0
    #create empty lists and sums for future reference

    for position,num in enumerate(part1):
            newnumber = num
            listofnum.append(newnumber)
    for position,num in enumerate(part2):
            newnumber = num
            listofnum.append(newnumber)
            #add each number separately in the list of numbers
    for position, number in enumerate(listofnum):
        if position%2==0:
            number = int(number)
            sum = number * 2
            listofsum.append(sum)
            #if the position of the number is even
            #multiply with 2
            #add each sum separately to the list of sums
        else:
            number = int(number)
            sum = number * 1
            listofsum.append(sum)
            #if the position of the number is not even
            #multiply with 1
            #add each sum separately to the list of sums
    for position, number in enumerate(listofsum):
        number = str(number)
        #convert the numbers to stringformat to ease the function and for the use of len(...)
        if len(number) == 2:
            number = int(number)
            newnumber = number-9
            total = total+newnumber
            #if the number is a two-digit number
            #remove nine from the two-digit number (we want each digit to stand on their own)
            #(example: 10 becomes 1+0, 11 becomes 1+1, 12 becomes 1+2)
            #it is the same as to remove nine from each number (ex: 10-9 = 1, 11-9 = 2 and so on)
            #add each new number to the totalsum
        else:
            number = int(number)
            total = total+number
            #if the number is a one-digit number
            #add directly to the totalsum

    while total+int(control) > 0:
        #while the totalsum is more than zero
        finalsum = total + int(control)
        #add the control number to the totalsum for a final sum
        if finalsum%10 == 0:
            return True
        else:
            return False
        #if the final sum is evenly divisible with 10
        #return True
        #if not
        #return False





print valid_pnr("970516-1488")
