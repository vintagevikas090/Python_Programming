''' Remove empty strings from a list of strings'''
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for i in str_list:
    if i == "":
        continue
    else:
        print(i)
