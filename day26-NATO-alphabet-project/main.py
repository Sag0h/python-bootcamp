import pandas

nano_phonetic_alphabet = pandas.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day26-NATO-alphabet-project\nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in nano_phonetic_alphabet.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()