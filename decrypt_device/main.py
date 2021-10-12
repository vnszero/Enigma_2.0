CEIL = 122
END_LINE = '\n'
FLOOR = 32
FOG_NUM = 1
FOG_POS = 2
ROLLBACK = 90
SECURITY = 'access denied\n'
SHIFT = 0

def verify_code(message : str) -> list:
    i = 0
    shift = None
    fog_num = None
    fog_pos = None
    code_message = ''
    for alpha in message:
        if i == SHIFT:
            shift = alpha
        elif i == FOG_NUM:
            fog_num = alpha
        elif i == FOG_POS:
            fog_pos = alpha
        else:
            code_message += alpha
        if alpha == END_LINE:
            with open("code.txt", "w") as file:
                file.write(SECURITY)
            break
        i+=1
    return shift, fog_num, fog_pos, code_message

def clear(message : str, fog_num : int, fog_pos : int) -> str:
    clear_message = ''
    i = FLOOR
    for alpha in message:
        if i > fog_num:
            i = FLOOR
        if i == fog_pos:
            clear_message += alpha
        i += 1
    return clear_message

def uncesar(message : str, shift : int) -> str:
    uncesar_message = ''
    for alpha in message:
        ord_ascii = ord(alpha)
        if ord_ascii < shift + FLOOR:
            uncesar_message += chr(ord_ascii+ROLLBACK-shift)
        else:
            uncesar_message += chr(ord(alpha)-shift)
    return uncesar_message

def main():
    try:
        # open, read and verify
        encrypt_message = ''
        with open("code.txt", "r") as file:
            encrypt_message = file.read()
        shift, fog_num, fog_pos, code_message = verify_code(encrypt_message)

        if shift != None and fog_num != None and fog_pos != None:
            # clear
            clear_message = clear(code_message, ord(fog_num), ord(fog_pos))

            # uncesar
            decrypt_message = uncesar(clear_message, ord(shift))

            # export
            with open('message.txt', 'w') as file:
                file.write(decrypt_message)
    except:
        print('There is a problem with: code.txt, Tip: verify the path')

if __name__ == '__main__':
    main()