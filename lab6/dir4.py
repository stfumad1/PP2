def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found")
        return -1
    except Exception as e:
        print("An error occurred:", e)
        return -1

file_name = input("Enter the file name: ")
lines_count = count_lines(file_name)

if lines_count != -1:
    print("Number of lines in the file:", lines_count)
