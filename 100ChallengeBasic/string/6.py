#############
#  OPTION1  #
#############


str_input = input()

str_input = str_input.swapcase()

str_input_reverse = "".join(reversed(str_input))

# OR for reversed String use line below :
# str_input_reverse = str_input[::-1]

print(str_input_reverse)
