import pandas

it_continues = True
while it_continues:
    #TODO 1. Create a dictionary in this format:
    #{"A": "Alfa", "B": "Bravo"}
    data = pandas.read_csv("nato_phonetic_alphabet.csv")

    alphabetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    try:
        word = input("Enter a word: ").upper()
        output_list = [alphabetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        it_continues = True
    else:
        it_continues = False
