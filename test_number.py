def valid_number(phonenumber):
    if len(phonenumber)==12:
        return True
    return False

k = valid_number("919492331133")
print(k)