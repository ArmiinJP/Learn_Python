
#############
#  OPTION1  #
#############
def delete_space_str(string):
    str_without_space = ""
    for char in string:
        if char == " ":
            pass
        else:
            str_without_space += char

    return str_without_space


input_str = input()

print(delete_space_str(input_str))

#############
#  OPTION2  #
#############
# input_str = input()
# str_without_space = input_str.replace(" ", "")
# print(str_without_space)
