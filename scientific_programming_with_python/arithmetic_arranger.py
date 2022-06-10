import re

def arithmetic_arranger(problems, solve = False):

  topline=""
  bottomline=""
  lineline=""
  sumline=""

  #Produce error if there is too many problems
  if(len(problems) >5):
    return "Error: Too many problems."

  #Search through each problem in problems and do the following
  for problem in problems:

    #If the problem contains any symbols except numbers 0-9 or + and - produc error
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]" , problem)) or (re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    #Split each problem into first number, second number and operator
    firstnumber =  problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondnumber = problem.split(" ")[2]
    #print( firstnumber, secondnumber, operator)

    #Find the sum depending on whether is add or subtract
    sum=""
    if (operator == "+"):
      sum = str(int(firstnumber) + int(secondnumber))
    elif (operator == "-"):
      sum = str(int(firstnumber) - int(secondnumber))
    #print (sum)

    #If either numbers are 5 or more digits produce an error
    if (len(firstnumber) >= 5 or len(secondnumber) >=5):
      return "Error: Numbers cannot be more than four digits."

    maxlength = max(len(firstnumber), len(secondnumber)) + 2 #max length +2 to work out how many "-" are needed
    #print (maxlength)
    top = str(firstnumber).rjust(maxlength) #top part is the first number alligned right with "maxlength" spaces
    bottom = operator + str(secondnumber).rjust(maxlength - 1) # bottom part is operator and second number
    lines= ""
    for s in range(maxlength): #Add the correct number of lines depending on max length
      lines += "-"
    suml = str(sum).rjust(maxlength)

    #if the problem is not the last problem then add four spaces, if it is then add none
    if problem != problems[-1]:
      top += '    '
      bottom += '    '
      lines += '    '
      suml += '    '
    else:
      top = top
      bottom = bottom
      lines = lines
      suml = suml

    #Adding each of the top bottom and lines parts to the overall string
    topline = topline + top
    bottomline = bottomline + bottom
    lineline = lineline + lines
    sumline = sumline + suml

  #combining each the strings to create the overall string
  #if the calculation needs to be solved then add the sumline to the string
  if solve:
    string = topline + "\n" + bottomline + "\n" + lineline + "\n" + sumline
  else:
    string = topline + "\n" + bottomline + "\n" + lineline
  return (string)

  
