import os
import pyaes

def decrypt_file(encrypted_file_name, decrypted_file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(encrypted_file_name, "rb") as file:
            file_data = file.read()

        # Configurar o AES para descriptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(encrypted_file_name)

        # Criar o arquivo descriptografado
        with open(decrypted_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo '{decrypted_file_name}' descriptografado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Nome do arquivo criptografado e nome do arquivo descriptografado
    encrypted_file = "teste.txt.ransomwaretroll"
    decrypted_file = "teste.txt"

    # Chave para descriptografia
    key = b"testeransomwares"

    # Chamar a função de descriptografia
    decrypt_file(encrypted_file, decrypted_file, key)
