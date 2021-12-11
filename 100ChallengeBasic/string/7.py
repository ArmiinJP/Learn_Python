

def is_repeated(char, string):
    count_char = string.count(char)
    if count_char > 1:
        return True
    else:
        return False


str_input = input()

repeated_char_list = []

for candidate in str_input:
    if ((is_repeated(candidate, str_input))
            and (candidate not in repeated_char_list)):
        repeated_char_list.append(candidate)


print("total number of repeated characters is: "
      f"{len(repeated_char_list)}")


if repeated_char_list:
    for char in sorted(repeated_char_list):
        print(char, end=" ")
    print("")
    # OR print member of list using line bellow :
    # print(*repeated_char_list)
else:
    print(None)
