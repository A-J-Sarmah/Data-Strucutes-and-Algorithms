def pallindrom_check(string):
    string_list = list(string)
    reversed_string_list = list(reversed(string_list))
    for i in range(len(string_list)):
        if string_list[i] != reversed_string_list[i]:
            return False
            break
    return True

value = input("Enter a string or number to check\n")
result = pallindrom_check(value)
if result:
    print(value, " is a pallindrom")
else:
    print(value , " isn't a pallindrom")