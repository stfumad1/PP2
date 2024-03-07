import string

def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = f"{letter}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is the content of file {file_name}")
            print(f"The file {file_name} generated completely.")

    except Exception as e:
        print(f"An error occurred: {e}")

generate_text_files()
