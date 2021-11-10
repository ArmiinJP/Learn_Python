

str_input = input()
str_output = ""

word_list = str_input.split(" ")


for word in word_list:
    low_word = word.lower()
    sort_low_word = "".join(sorted(low_word))
    str_output = str_output + sort_low_word + " "


str_output.rsplit(" ")
print(str_output)
