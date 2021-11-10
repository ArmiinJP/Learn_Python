
def is_pre_in_string(string, prefix):
    if string.find(prefix) == 0:
        return True
    else:
        return False


str_input = input("Please Enter String : ")
pre_input = input("Please Enter Prefix : ")

print(is_pre_in_string(str_input, pre_input))
