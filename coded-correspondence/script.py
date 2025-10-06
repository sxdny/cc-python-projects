# Coded Correspondence

vocab = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# t = 19 --> f = 5 == 19 + 5 == y
# x = 23 --> r = 17 --> 24 + 17 = 41 --> 25 - 23 = 2 que YA HEMOS HECHO --> 17 - 2 = 15 - 1 --> O

signs = [".", "?", "!"]

offset = 10

# Encrypt word function
def encrypt_word(word: str, offset=offset) -> str:
    word_to_list = [char.upper() for char in word]
    word_encrypted_list = []
    for char in word_to_list:
        for i, letter in enumerate(vocab):
            if char == letter:
                word_encrypted_list.append(vocab[i - offset])

    return "".join(word_encrypted_list)
    # C --> offset = -10 --> 2 - 10 = -8 <-- indice que tenemos que acceder

def decrypt_word(encr_word: str, offset=offset) -> str:
    encr_word_to_list = [char.upper() for char in encr_word]
    word_decrypted_list = []
    
    for char in encr_word_to_list:
        for i, letter in enumerate(vocab):
            if char == letter:
                # si la suma es mayor, significa que se pasa y hay que restar los movimientos restantes...
                # por ejemplo, la S se encuentra en el indice 18
                # el ultimo indice disponible de vocab es 25
                # si sumamos 18 + el offset = 28, y esto no funcionaria
                # entonces hay que saber el n de movimientos restantes a la derecha que me falta
                # hacemos la resta de 25 - 18 = 7 movimientos que he hecho
                # si hemos hecho 7 movimientos, signfica que nos quedan 3, porque el offset es de 10
                # ahora lo único que nos queda, es simplemente acceder al indice mov_que_nos_falta - 1 = 2
                # esto nos da que S == C
                if i + offset > len(vocab) - 1:
                    def_index = offset - (len(vocab) - 1 - i) - 1 # los -1s son por el indice
                    word_decrypted_list.append(vocab[def_index])
                else:
                    word_decrypted_list.append(vocab[i + offset])
    
    return "".join(word_decrypted_list)

def decrypt_sentence(sentence: str, offset=offset) -> str:
    # string --> list
    sentence_list = sentence.split(" ")
    sentence_list_fixd = [word.replace("\n", "") for word in sentence_list]
    
    # separamos los puntos
    sentence_list_expanded = []
    for word in sentence_list_fixd:
        if "!" in word:
            word_sepr = word.split("!")
            word_sepr[1] = "!"
            sentence_list_expanded.append(word_sepr)
        elif "?" in word:
            word_sepr = word.split("?")
            word_sepr[1] = "?"
            sentence_list_expanded.append(word_sepr)
        elif "." in word:
            word_sepr = word.split(".")
            word_sepr[1] = "."
            sentence_list_expanded.append(word_sepr)
        else:
            sentence_list_expanded.append(word)
    
    decr_sentence_list = []
    
    for word in sentence_list_expanded:
        if type(word) == list:
            word_to_decr = "".join(word[0])
            decr_sentence_list.append(decrypt_word(word_to_decr, offset))
            decr_sentence_list.append(word[1])  # añadimos el signo que tiene
        else:
            decr_sentence_list.append(decrypt_word("".join(word), offset))
    
    # lo pasamos a string
    decr_sentence_string = ""
    li = len(decr_sentence_list) - 1
    
    for i, word in enumerate(decr_sentence_list):
        if not i >= li:
            # comprobamos si el siguiente elemento es un signo
            if decr_sentence_list[i + 1] in signs:
                string_to_append = word.lower()
                decr_sentence_string += string_to_append
            # comprobamos si hay que poner mayúscula
            elif decr_sentence_list[i - 1] in signs:
                decr_sentence_string += word.title() + " "
            else:
                decr_sentence_string += word.lower() + " "
    
    return decr_sentence_string
    
# tenemos las funciones hechas, ahora, a probar de desencriptar y encriptar textos

encr_text = """
xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
"""

def string_to_list(sentence: str) -> list:
    # returns a list with words and puntuaction separated
    strlist = sentence.split(" ")
    str_fxd = [word.replace("\n", "") for word in strlist]
    str_expd = []
    for word in str_fxd:
        if "!" in word:
            word_sepr = word.split("!")
            word_sepr[1] = "!"
            str_expd.append(word_sepr)
        elif "?" in word:
            word_sepr = word.split("?")
            word_sepr[1] = "?"
            str_expd.append(word_sepr)
        elif "." in word:
            word_sepr = word.split(".")
            word_sepr[1] = "."
            str_expd.append(word_sepr)
        else:
            str_expd.append(word)
    return str_expd


encr_text_list = encr_text.split(" ")
encr_text_list_fixd = [word.replace("\n", "") for word in encr_text_list]

# separamos los puntos de intr, excl, puntos, etc
encr_text_list_fixd_expanded = []
for word in encr_text_list_fixd:
    if "!" in word:
        word_sepr = word.split("!")
        word_sepr[1] = "!"
        encr_text_list_fixd_expanded.append(word_sepr)
    elif "?" in word:
        word_sepr = word.split("?")
        word_sepr[1] = "?"
        encr_text_list_fixd_expanded.append(word_sepr)
    elif "." in word:
        word_sepr = word.split(".")
        word_sepr[1] = "."
        encr_text_list_fixd_expanded.append(word_sepr)
    else:
        encr_text_list_fixd_expanded.append(word)

decr_text_list = []

# ahora, usamos la función para desencriptar cada palabra:
for word in encr_text_list_fixd_expanded:
    if type(word) == list:
        word_to_decr = "".join(word[0])
        decr_text_list.append(decrypt_word(word_to_decr))
        decr_text_list.append(word[1]) # añadimos el signo que tiene
    else:
        decr_text_list.append(decrypt_word("".join(word)))
    

# ahora, lo pasamos a un string
decr_text_string = ""
last_index = len(decr_text_list) - 1

for i, word in enumerate(decr_text_list):
    if not i >= last_index:
        # comprobamos si el siguiente elemento es un signo
        if decr_text_list[i + 1] in signs:
            string_to_append = word.lower()
            decr_text_string += string_to_append
        # comprobamos si hay que poner mayúscula
        elif decr_text_list[i - 1] in signs:
            decr_text_string += word.title() + " "
        else:
            decr_text_string += word.lower() + " "

# falta desencriptar sin saber el offset. basicamente le asignamos el offset manualmente, como ya he hecho y añadido arriba

# asignamos un offset de 10 en este caso
#print(decrypt_sentence(encr_text, 10))

# vigenere cypher

# movemos a la izquierda cuantas veces sea el valor del indice de la
# letra de la palabra que hemos escogido.
# ejemplo: barry --> original
# dog --> palabra para cifrar

# cubrimos la palabra 'barry' con dog, repitiendola:
# dogdo

# y ahora. 'b' está en el indice 1 del abc
# y la 'd' esta en el 3, por lo que movemos
# 3 veces a la izquierda desde el indice de y

# nos queda la posición 24, o 'y'.
# y así para cada palabra

# ahora, a desencriptar el mensaje
encr_text_vc = """
txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!
"""

keyword = "friends"

vc_list = string_to_list(encr_text_vc)

#print(vc_list)

# ahora, tenemos que desencriptar la frase usando 'keyword'
# movemos a la derecha porque estamos desencriptando

key_list = [char for char in keyword]
#print(key_list)

len_vc_list = len(vc_list)
len_key = len(key_list)

indx = 0
indx_key = 0

decr_vc_list = []

for i, segment in enumerate(vc_list):
    if type(segment) == list:
        word_to_append = []
        # separar el punto con la palabra...
        word = segment[0]
        for char in word:
            
            if indx_key == len_key:
                indx_key = 0
                
            index_char = 0
            index_key = 0
            
            for i, letter in enumerate(vocab):
                if char.upper() == letter:
                    index_char = i
                if key_list[indx_key].upper() == letter:
                    index_key = i
            
            # calcular el indice del valor desencriptado
            index_decr_letter = index_char + index_key
            
            if index_decr_letter > len(vocab) - 1:
                movs_ya_hechos = len(vocab) - 1 - index_char
                nuevo_indice = index_key - movs_ya_hechos - 1
                word_to_append.append(vocab[nuevo_indice].lower())
            else:
                word_to_append.append(vocab[index_decr_letter].lower())
            indx_key += 1
        word_to_append.append(segment[1])
        decr_vc_list.append(word_to_append)
    else:
        word_to_append = []
        for char in segment:
            if indx_key == len_key:
                indx_key = 0
            #print(f"Letra {char} con {key_list[indx_key]}")
            # calcular el valor del indice desencriptado ok?
            index_char = 0
            index_key = 0

            for i, letter in enumerate(vocab):
                if char.upper() == letter:
                    index_char = i
                if key_list[indx_key].upper() == letter:
                    index_key = i
            
            index_decr_letter = index_char + index_key
            if index_decr_letter > len(vocab) - 1:
                movs_ya_hechos = len(vocab) - 1 - index_char
                nuevo_indice = index_key - movs_ya_hechos - 1
                word_to_append.append(vocab[nuevo_indice].lower())
            else:
                word_to_append.append(vocab[index_decr_letter].lower())
            indx_key += 1
        decr_vc_list.append(word_to_append)

# ahora tengo la lista, lo convertimos a un string legible porfa
vc_list_to_string = ""

for word in decr_vc_list:
    vc_list_to_string = vc_list_to_string + "".join(word) + " "

print(vc_list_to_string)


