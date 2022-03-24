# adewale #

TO_REPLACE = "[name]"

# turn each line of the txt file to a list
data = open("./Input/recipient_names.txt")
data_list = data.readlines()
# print(data_list)

# remove '\n' from each list item
clean_data_list = []
for b in data_list:
    stripped_b = b.strip("\n")
    clean_data_list.append(stripped_b)
# print(clean_data_list)

# read the letter and save in a variable
with open("./Input/letter.txt") as data2:
    the_data2 = data2.read()
    # print(the_data2)

# replace [name] with each recipient name and save a txt file per
# recipient in a separate folder
for i in clean_data_list:
    data2_final = the_data2.replace(TO_REPLACE, i)
    # print(data2_final)
    with open(f"./Output/letter_to_{i}.txt", "w") as file:
        file.write(data2_final)
