
import string

# alphabet = [
#     'a', 'b', 'c',
#     'd', 'e', 'f',
#     'g', 'h', 'i',
#     'j', 'k', 'l',
#     'm', 'n', 'o',
#     'p', 'q', 'r',
#     's', 't', 'u',
#     'w', 'x', 'y',
#     'z',
# ]


def is_alphas_exist(itr_str):
    for char in string.ascii_lowercase:
        if char in itr_str:
            continue
        else:
            return False
    return True


input_str = input()
set_input_str_low = set(input_str.lower())

print(is_alphas_exist(set_input_str_low))

