from sys import argv

def sort_dec(num):
  toRet = ""
  it = list(str(num))
  it.sort()
  it = it[::-1]
  for i in it: toRet += str(i)
  toRet = int(toRet)
  return toRet


def convert_to_four_digit(num):
  theStr = str(num)
  theLen = len(theStr)
  if theLen < 4:
    for i in range(4 - theLen):
      theStr = "0" + theStr
    return theStr
  if theLen == 4: return num


def the_condition(num):
  if 9999 >= int(num) >= 1000:
    daStr = str(num)
    if int(daStr[0]) == int(daStr[1]) == int(daStr[2]) == int(daStr[3]):
      print("The Number cannot be all of one digit.")
      return False
    else: return True
  else:
    print("Number should be of 4 digits.")
    return False


def kaprekar_constant(num):  
  THE_CONSTANT = 6174
  result = num
  counter = 0

  if the_condition(num):
    print("Starting with {}".format(result))

    while result != THE_CONSTANT:
      counter += 1
      print("# Loop {} #".format(counter))
      reordered = sort_dec(result)
      print("Reordered: {}".format(reordered))
      reverse = str(reordered)[::-1]
      print("Reversed: {}".format(reverse))
      result = reordered - int(reverse)
      result = convert_to_four_digit(result)
      print("Result after Subtraction: {}".format(result))
      print(" ")
      
  if result == THE_CONSTANT:
    print("Reached the kaprekar's constant in {} loops!".format(counter))
  else: print("Did not Reach the Constant!")


if argv and len(argv) > 1:
  kaprekar_constant(argv[1])
else: print("please provide a number")
