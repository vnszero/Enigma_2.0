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
    
    # verify empty message
    if pre_message != '':
        # ascii
        alpha = list()
        for i in range(91):
            alpha.append(i+31)

        # the set
        new_message = ''

        # random dictionary with the new codes
        random_pos = dict()
        while len(alpha) != 0:
            new_pos = random.randint(0,len(alpha)-1)
            new_message = new_pos+'{'
            l = len(alpha)
            random_pos[l] = alpha.pop(new_pos)

        print(random_pos)

        # message content
        for token in pre_message:
            code = chr(random_pos[ord(token)-32])
            new_message += code
            #print(ord(token)-ord(code))

        #print(new_message)

if __name__ == '__main__':
    main()