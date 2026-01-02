words= "My name is kayode"

def capitalize(words):
    new_words = words.split()
    for word in new_words:
        for index , letter in enumerate(word):
            if index == 0 :
                new_letter = word[index].upper()
            else :
                new_letter = word[index].lower()
            result = new_letter
            print(result , end="")
capitalize(words)

print("just a challenge not a part of this project")
