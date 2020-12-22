def encrypt(number, key):
    """
    Input:
        1. number to be encrypted
        2. key of the caesar cypher
    Output: Encrypted number

    >>> encrypt(1234, 3)
    4567
    >>> encrypt(395, 5)
    840
    """

    encrypted = ''
    num_as_str = str(number) # '1234'
    for digit in num_as_str:
        num = int(digit) # 1 or 2 or 3 or 4 as integer
        shifted_num = (num + key) % 10
        encrypted += str(shifted_num)

    return int(encrypted)


def decrypt(encrypted_number, key):
    """
    >>> decrypt(4567, 3)
    1234
    >>> decrypt(840, 5)
    395
    """
    return encrypt(encrypted_number, -1*key)


def hack(encrypted_number):
    # For numbers, hack might not work because every number is possible
    # Find a way if you can
    pass


def hack_english_sentence(sentence):
    # 1. try to encrypt using 1 to 26
    # 2. count how much english in each resulted sentence
    # 3. return the one that has more english
    pass




# 1 -> 26

# hgdfy sd sdfs isfgfg
# 1:  jhifu js dkjs dhdhsr      0
# 2:                            1
# 3:                            0
# 4:                            2
# 5: hevlo gf dhjm jjdjde
# 6: hello ms ayah welcome      3
# .
# .
# 26:






