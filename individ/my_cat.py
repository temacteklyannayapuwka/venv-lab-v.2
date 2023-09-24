import sys

def cat_files(file_names):
    for file_name in file_names:
        try:
            with open(file_name, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Skipping...")
        except Exception as e:
            print(f"An error occurred while reading '{file_name}': {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py file1 file2 ...")
    else:
        file_names = sys.argv[1:]
        cat_files(file_names)
