# it not work like this
one_time_pad = [8, 18, 4, 12, 3, 1, 12, 2, 0, 6, 6, 7, 13, 17, 10, 7, 4, 19, 15, 0, 1, 0, 10, 1, 11, 15, 16, 7, 12, 11, 0, 3, 2, 25, 2, 0, 22, 22, 14, 18, 3, 11, 6]

message_list = ["LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl", 
                "WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs",
                "UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg",
                "LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu",
                "LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp"]

def translate(letter, key):
    capital = False
    if letter.isupper():
        capital = True 
        letter = letter.lower()

    new = ord(letter) + key 
    if new > 122:
        new -= 26
  
    if capital:
        return chr(new).upper()
    else:
        return chr(new)

print(len(one_time_pad), len(message_list[1]))

for message in message_list:
    print(message, "= ", end="")
    for index, key in enumerate(one_time_pad):
        if index == len(message):
            break
        print(translate(message[index], key), end="")
    print()

