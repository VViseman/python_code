# -*- coding: utf-8 -*-

import Crypto.Cipher.AES

# キーは16, 24, 32バイトの長さでなければならない
obj = Crypto.Cipher.AES.new('This is a key456', Crypto.Cipher.AES.MODE_ECB)
message = "The answer is no"  # 文字数は16の倍数でなければならない
ciphertext = obj.encrypt(message)
obj2 = Crypto.Cipher.AES.new('This is a key456', Crypto.Cipher.AES.MODE_ECB)
decrypt = obj2.decrypt(ciphertext)
print "message:", message
print "encrypt:", ciphertext
print "decrypt:", decrypt

import Crypto.Cipher.DES

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = Crypto.Cipher.DES.new("abcdefgh", Crypto.Cipher.DES.MODE_ECB)
plain = "Guido van Rossum is a space alien."
# 文字数は8の倍数でなければエラーになるのでplainに６文字結合する
ciph = obj.encrypt(plain + "XXXXXX")
decrypt = obj.decrypt(ciph)
print "plain  :", plain
print "encrypt:", ciph
print "decrypt:", decrypt

