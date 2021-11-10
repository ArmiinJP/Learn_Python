
def is_pre_in_string(string, suffix):
    return string[len(string)-len(suffix):] == suffix
    # return string.endswith(suffix)


str_input = input("Please Enter String : ")
suf_input = input("Please Enter suffix : ")

print(is_pre_in_string(str_input, suf_input))
