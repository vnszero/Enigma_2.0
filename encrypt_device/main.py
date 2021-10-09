import random
def word_steam(message : str) -> str:
    #remove acent
    in_table = "áéíóúâêôçãẽõü"
    out_table = "aeiouaeocaeou"
    no_accents = message.translate(''.maketrans(in_table, out_table))

    fixed_message = no_accents
    return fixed_message

def main():
    message = input('Enter your message: ')
    pre_message = word_steam(message)
    
    # ascii
    alpha = list()
    for i in range(91):
        alpha.append(i+32)

    # random dictionary with the new codes
    random_pos = dict()
    while len(alpha) != 0:
        new_pos = random.randint(0,len(alpha)-1)
        random_pos[len(alpha)-1] = alpha.pop(new_pos)

    # new message
    new_message = ''
    for token in pre_message:
        new_message += chr(random_pos[ord(token)-32])
        print(ord(token)-32)

    print(new_message)

if __name__ == '__main__':
    main()