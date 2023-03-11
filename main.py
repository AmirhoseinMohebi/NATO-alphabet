import pandas
data = pandas.read_csv('./nato_phonetic_alphabet.csv')
new_d = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_d)
user_input = input("Enter a word... ").upper()
new_word = [new_d[letters] for letters in user_input]
print(new_word)
