import random

FLOOR = 32
ROLLBACK = 90
CEIL = 122

def word_steam(message : str) -> str:
    #remove acent
    in_table = "áéíóúâêôçãẽõü"
    out_table = "aeiouaeocaeou"
    no_accents = message.translate(''.maketrans(in_table, out_table))

    fixed_message = no_accents
    return fixed_message

def cesar_shift(message : str) -> list:
    shift = random.randint(FLOOR,CEIL)
    cesar_message = ''
    for alpha in message:
        code = ord(alpha) + shift
        if code > CEIL:
            code -= ROLLBACK
        cesar_message += chr(code)
    #return message, shift
    return cesar_message, shift

def fog_maker(message : str) -> list:
    fog_num = random.randint(FLOOR,CEIL) # don't use A to avoid weak codes
    fog_pos = random.randint(FLOOR, fog_num) # don't use A to avoid weak codes
    fog_message = ''
    for alpha in message:
        i = 1
        while i <= fog_num:
            if i == fog_pos:
                fog_message += alpha
            else:
                smog = random.randint(FLOOR,CEIL)
                fog_message += chr(smog)
            i+=1 
    #return message, fog_num, fog_pos
    return fog_message, fog_num, fog_pos

def main():
    message = input('Enter your message: ')
    pre_message = word_steam(message)
    
    # verify empty message
    if pre_message != '':
        # Cesar Code
        cesar_message, shift = cesar_shift(pre_message)

        # fog_maker
        fog_message, fog_num, fog_pos = fog_maker(cesar_message)

        # zip
        crypt_message = chr(shift) + chr(fog_num) + chr(fog_pos) + fog_message

        # export
        print(crypt_message)
        with open('code.txt', 'w') as file:
            file.write(crypt_message)

if __name__ == '__main__':
    main()