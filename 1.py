
# -----------------
# Option 1
# -----------------
import re

input_string = input()
print(re.sub('[,]', ".", input_string))

# -----------------
# Option 2
# -----------------
input_string = input()
print(input_string.replace(',', '.'))
