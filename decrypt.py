import os
import pyaes

## Abrir o arquivo a ser criptografado
file_name = 'teste.txtransowaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Definir a chave de descriptografia
key = b'testeransowares1'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo encriptografado
os.remove(file_name)

## Criar um novo arquivo descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
