vocabulary_words={"tuple": "immutable string","concatenate": "add","len": "length","int": "integer",}

def count_key():
	character_dict = {}
	name = "grace durham"

	for character in name:
		if character in character_dict:
			character_dict[character] +=1
		else:
			character_dict[character] =1

	return character_dict
print count_key()
