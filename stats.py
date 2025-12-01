def get_word_count(text):
    number = 0
    words = text.split()
    for word in words:
        number = number +1
    return(number)

def get_letter_count(text):
    alphabet={}
    text=text.lower()
    for letter in text:
        letter=letter.lower()
        if not ("a" <= letter <= "z"):
            continue
        elif letter not in alphabet:
            alphabet[letter] = 1
        elif letter in alphabet:
            alphabet[letter]=alphabet[letter]+1
        #print(f"letter is {letter} with count {alphabet[letter]}")
    return alphabet