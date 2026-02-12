import os
import base64

def base64_to_png(input_folder, output_folder):
    """
    Convert a Base64 string into a PNG file.
    """
    for file in os.listdir(input_folder):
        if not (file.lower().endswith(".txt")):
            continue

        input_path = os.path.join(input_folder, file)
        output_name = os.path.splitext(file)[0] + ".png"
        output_path = os.path.join(output_folder, output_name)

        with open(input_path, "r") as f:
            b64_str = f.read()
        img_data = base64.b64decode(b64_str)

        with open(output_path, "wb") as png_file:
            png_file.write(img_data)


if __name__ == "__main__":

    DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    INPUT_FOLDER = os.path.join(DESKTOP, 'TOUPDATE')
    OUTPUT_FOLDER = os.path.join(DESKTOP, 'UPDATED')

    base64_to_png(INPUT_FOLDER, OUTPUT_FOLDER)

    print("PNG output saved.")
