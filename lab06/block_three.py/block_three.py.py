def replace_colons(input_string):

  original_length = len(input_string)
  modified_string = input_string.replace(":", "%")
  return modified_string


input_string = "why? :::::: why?"
modified_string, count = replace_colons(input_string)
print(f"Original: {input_string}")
print(f"Modified: {modified_string}")