import base64
import json
from pathlib import Path

def decode_base64_file(input_file: str, output_file: str) -> None:
    """
    Decodes a base64 encoded file and writes the output to a specified file as formatted JSON.

    Parameters:
    input_file (str): The path to the base64 encoded file.
    output_file (str): The path to the output decoded file.
    """
    try:
        # Read the base64 encoded file
        encoded_data = Path(input_file).read_text()
        
        # Decode the base64 content
        decoded_data = base64.b64decode(encoded_data)
        
        # Convert the decoded data to JSON
        json_data = json.loads(decoded_data)
        
        # Write the formatted JSON data to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        
        print(f"File decoded successfully and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
