import os
from decoder import decode_base64_file

def main():
    # Defina os caminhos dos arquivos aqui
    input_file = os.path.join("file", "encoded_file.txt")
    output_file = os.path.join("file", "decoded_output.json")
    
    decode_base64_file(input_file, output_file)

if __name__ == "__main__":
    main()
