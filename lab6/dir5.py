def write_to_file(file_name, string_list):
    try:
        with open(file_name, 'w') as file:
            for item in string_list:
                file.write(item + '\n')
        print(file_name)
    except Exception as e:
        print(e)

string_list = input("").split()
file_name = input("")

write_to_file(file_name, string_list)
