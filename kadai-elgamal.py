# -*- coding: utf-8 -*-

import random
import sympy

#plain_textを数値にする,復号化で得られたdecodeを平文にする
def code( word ):
    result = []
    for letter in word:
        result.append( ord(letter) )
    return result

def make_prime( M, N ):
    while True:
        n = random.randint( M, N )
        i = 2
        flag = True
        while i*i <= n and flag:
            if n % i == 0:
                flag = False
            i += 1
        if flag:
            return n

#modの計算
def calc_mod( a, b, p ):
    result = 1
    for i in range(b):
        result = ( result * a ) % p
    return result

#pk(公開鍵の要素)、sk(秘密鍵の要素)を(p, g, y)としてランダムに生成する
def key_generate( k ):
    a = 1 << (k-1)
    b = 1 << k
    p = make_prime( a, b )
    g = sympy.primitive_root(p)
    x = random.randint( 0, p-1 )
    y = calc_mod( g, x, p )
    return ( p, g, y ), x

# plain_textをpkを使って暗号化する

def encrypt(m, pk):
    cipher = []
    p, g, y = pk
    r = random.randint( 0, p-1 )
    c1 = calc_mod( g, r, p )
    for l in m:
        c2 = ( ord(l) * calc_mod( y, r, p ) ) % p
        cipher.append( c2 )
    return ( c1, cipher )

# plain_textをcipher, pk, skを使って復号化する
def decrypt( c, pk, sk ):
    decode = ''
    c1, c2 = c
    p, g, y = pk
    x = sk
    d = calc_mod( c1, p-1-x, p )
    for cc in c2:
        m = ( cc * d ) % p
        decode += chr( m )
    return decode

#main文
if __name__ == '__main__':
#    pk, sk = key_generate(8)
    pk, sk = ((13, 2, 3),2)
    plain_text = 'You can always become better.'
#    plain_text = '1234567'
    plain_code = code(plain_text)     # plain_textを文字コードにする
#    cipher = encrypt(plain_text, pk)  # plain_textをpkを使って暗号化する
    cipher = encrypt(plain_text, ((13, 2, 3), 2))  # plain_textをpkを使って暗号化する
    decode = decrypt(cipher, pk, sk)  # plain_textをcipher, pk, skを使って復号化する
    decode_code = code( decode )      # 復号化で得られたdecodeを平文にする

    print('公開鍵 ( p, g, y ) = ', pk)
    print('秘密鍵 x = ',sk) #ランダムな値が秘密鍵で与えられてもちゃんと復号できる。
    print('平文（文字コード） = ')
    print(plain_code)
    print('暗号 ( c1, c2 ) = ')
    print(cipher)
    print('復号（文字コード） = ')
    print(decode_code)
    print("復号  m'=", decode)

#    print( '公開鍵 ( p, g, y ) = ', pk )
#    print( '秘密鍵 x = ', sk )
#    print( '平文（文字コード） = ', plain_code )
#    print( '暗号 ( c1, c2 ) = ', cipher )
#    print( '復号（文字コード） = ', decode_code )
#    print( "復号　m'=", decode )
