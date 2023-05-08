def counter (name):
   
    name = name.replace(' ', '')
    if len(name) == 0:
        raise Exception("Please input your name")
    if name.isalpha():
     return len(name)
    else:
     raise("The name needs to be in English letters")


