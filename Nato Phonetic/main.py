import pandas

data=pandas.read_csv("phonetic.csv")
df=data.to_dict()

phonetic={row.letter:row.code for (index,row) in data.iterrows()}

#dictionary comprehension
word=input("Enter a word:\n").upper()

#list comprehension
#[new_item for item in item]
output=[phonetic[letter] for letter in word]

print(output)