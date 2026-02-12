import os
import base64

def png_to_base64(input_folder, output_folder):
    """
    Convert a PNG file to a Base64 string.
    """
    for file in os.listdir(input_folder):
        if not file.lower().endswith(".png"):
            continue

        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0] + ".txt"
        output_path = os.path.join(output_folder, output_name)

        with open(input_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode("utf-8")

        with open(output_path, "w") as txt_file:
            txt_file.write(encoded)


if __name__ == "__main__":
    
    DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    INPUT_FOLDER = os.path.join(DESKTOP, 'TOUPDATE')
    OUTPUT_FOLDER = os.path.join(DESKTOP, 'UPDATED')

    png_to_base64(INPUT_FOLDER, OUTPUT_FOLDER)

    print("Base64 output saved.")
