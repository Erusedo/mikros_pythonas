# this code turns every vowel into the letter "g" and "G"

def translate(phrase):                  # learn how to use upper & lower case
    translation = ""                    # in -> checks if there is something in that string 
    for letter in phrase:                   
        if letter in "AEIOUaeiou":      # if letter.lower() in "aeiou":  
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

