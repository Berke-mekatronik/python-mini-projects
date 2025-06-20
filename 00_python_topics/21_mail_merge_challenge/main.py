PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter_content = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter_content)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter_content)

